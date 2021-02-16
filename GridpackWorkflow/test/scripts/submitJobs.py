#!/usr/bin/env python
import os
import sys
from optparse import OptionParser

########   customization start #########
pr = OptionParser(usage="%prog [options]")

#Model type, experimental labels
pr.add_option("--tag"         , dest="tag"       , type="string"      , default="" , help="An identifier of the run, please take into account that the code will rewrite files by default, so change tag accordingly")
pr.add_option("-f","--force"  , dest="force"     , action="store_true", default=False , help="Force temp folder recreation and just overall ignore warnings.")
pr.add_option("-o","--out"    , dest="out"       , type="string"      , default=os.getcwd(), help="Output folder for gridpacks, default is running one which probably is a bad idea")
pr.add_option("-i","--in"     , dest="inF"        , type="string"      , default=None, help="Input folder with the cards")
pr.add_option("-q","--queue"  , dest="queue"     , type="string"      , default="tomorrow", help="Condor queue to be used. Default is tomorrow (1 day). Other logical options are testmatch (3 days), nextweek (1 week), workday (8 hours)" )
pr.add_option("-j","--jobs"   , dest="jobs"      , type="int"         , default="8", help="Request this number of cores per job" )
pr.add_option("-p","--pretend", dest="pretend"   , action="store_true", default=False , help="Only create folders, don't run anything")
pr.add_option("-m","--mode"   , dest="mode"      , type="string"      , default="lxplus", help="Mode running: lxplus (default, will access the input cards through afs/eos), connect (will access and output everything through your stash area, remember to clean it afterwards!), slurm (will use slurm-like syntax)")


(options, args) = pr.parse_args()

########   customization end   #########

print options.force
if (os.path.isdir("tmp%s"%options.tag) or os.path.isdir("batchlogs%s"%options.tag) or os.path.isdir("exec%s"%options.tag)) and not(options.force):
  raise RuntimeError("Warning, some temp folders exists and you are risking overwriting them. If you are sure of what you are doing run in force mode (-f).")
else:
  os.system("rm -rf tmp%s"%options.tag)
  os.system("rm -rf exec%s"%options.tag)
  os.system("rm -rf batchlogs%s"%options.tag)
print 'I will create some submission temp folders for the logs for you...'

os.system("mkdir tmp%s"%options.tag)
os.system("mkdir exec%s"%options.tag)
os.system("mkdir batchlogs%s"%options.tag)
if "/afs/" in options.out and not(options.force):
  raise RuntimeError("Warning, you are sending your final gridpacks to be copied to afs, this might be a bad idea unles you have dedicated space for them. Run with force mode (-f) to force this.")
elif not(os.path.isdir(options.out)):
  os.system("mkdir %s"%options.out)

x = 0
##### loop for creating and sending jobs #####
for folder in os.listdir(options.inF):
    inputFolder = options.inF + "/" + folder
    files = os.listdir(inputFolder)
    # Do some basic checks
    if not( any(["run" in f for f in files]) and any(["proc" in f for f in files])): 
      print "Warning, folder %s does not seem to contain a run and proc card, will skip it for submission"%(inputFolder)
      continue
    ##### creates jobs #######
    with open('exec%s/job_'%options.tag+str(x)+'.sh', 'w') as fout:

      fout.write("#!/bin/sh\n")

      fout.write("#First we do a sparse checkout of genproductions to avoid copying the whole thing and to also have the latests set of patches available\n")

      fout.write("# We might want to fix a commit sha here to ensure it doesn't pull some tricks\n")
      fout.write("git clone https://github.com/cms-sw/genproductions.git --no-checkout genproductions --depth 1\n")
      fout.write("cd genproductions\n")
      fout.write("git config core.sparsecheckout true\n")
      fout.write("echo Utilities/scripts/ >> .git/info/sparse-checkout\n")
      fout.write("echo MetaData >> .git/info/sparse-checkout\n")
      fout.write("echo bin/MadGraph5_aMCatNLO >> .git/info/sparse-checkout\n")
      fout.write("git read-tree -m -u HEAD\n")
      fout.write("cd bin/MadGraph5_aMCatNLO/\n")

      fout.write("#Copy input cards\n")
      if options.mode == "lxplus": fout.write("cp -r %s Cards\n"%inputFolder)
      elif options.mode == "connect": fout.write("xrdcp root://stash.osgconnect.net:1094/%s Cards/\n"%(inputFolder.replace("/stash","")))
      fout.write("#Run the script\n")
      fout.write("sh gridpack_generation.sh %s Cards\n"%folder)
      fout.write("#Copy the gridpack back to somewhere readable\n")
      if options.mode == "lxplus": fout.write("mv *.tar.xz %s\n"%options.out)
      elif options.mode == "connect": fout.write("xrdcp *.tar.xz root://stash.osgconnect.net:1094/%s \n"%(options.out.replace("/stash","")))
      fout.write("#Do some cleanup just to be tidy\n")
      fout.write("cd ../../../\n")
      fout.write("rm -rf genproductions\n")

    os.system("chmod 755 exec%s/job_"%options.tag+str(x)+".sh")
    x += 1 
###### create submit.sub file ####
    
with open('submit.sub', 'w') as fout:
    fout.write("executable              = $(filename)\n")
    fout.write("arguments               = $(ClusterId)$(ProcId)\n")
    fout.write("output                  = batchlogs%s/$(ClusterId).$(ProcId).out\n"%options.tag)
    fout.write("error                   = batchlogs%s/$(ClusterId).$(ProcId).err\n"%options.tag)
    fout.write("log                     = batchlogs%s/$(ClusterId).log\n"%options.tag)
    fout.write("RequestCPUs             = %s\n"%options.jobs)
    if options.mode == "lxplus": fout.write('+JobFlavour = "%s"\n' %(options.queue))
    fout.write("\n")
    fout.write("queue filename matching (exec%s/job_*sh)\n"%options.tag)
    
###### sends bjobs ######
if not options.pretend:
  os.system("echo submit.sub")
  os.system("condor_submit submit.sub")
   
  print
  print "Your jobs are here:"
  os.system("condor_q")
  print
  print 'END'
  print
