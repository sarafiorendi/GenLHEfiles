#!/usr/bin/python
import os, sys
import ROOT as r
r.gROOT.SetBatch(True)
r.PyConfig.IgnoreCommandLineOptions = True
from DataFormats.FWLite import Events, Handle, Lumis
import glob
from collections import OrderedDict


# To measure the filter eff you can use local samples or access files remotely via cms-xrd-global.cern.ch/xrootd-cms.infn.it
# for remote access start your voms proxy

#fileBase = "/hadoop/cms/store/user/scasasso/mcProduction/AODSIM/T2bW_X05_dM-10to80/T2bW_X05_dM-10to80_genHT-160_genMET-80_{0}.root"
#fileBase = "root://cms-xrd-global.cern.ch///store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/6D0540CE-2D04-3B42-A26B-E8777B3C0924.root"

# Another option, without processing samples is to access the full dataset via dasgoclient
# Let's follow the example for the signal samples SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1
# First, query dasgoclient interactively to get the location of all the sample files and save it
#dasgoclient -query="file dataset=/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1/MINIAODSIM" > T2tt_2018.txt

# Name of the output root file
YEAR="2018"
hfilename='filterEffs_SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1_'+YEAR+'.root'

def main():
    fileList = []
    # .txt filename where you saved the samples files from dasgoclient
    samplesFileName = "T2tt_"+YEAR+".txt"
    number_of_lines = len(open(samplesFileName).readlines())
    samplesFile = open(samplesFileName)
    samples = samplesFile.readlines()
    for sample in samples:
      # Change servers in case the script fails in a specific file
      #fileList += ["root://cms-xrd-global.cern.ch/"+sample.replace('\n', '')]
      fileList += ["root://xrootd-cms.infn.it/"+sample.replace('\n', '')]
    #print fileList

    #fileList = [fileBase.format(i) for i in range(1,101)] # for samples saved locally
    #fileList = [fileBase] # in case you're using only 1 file remotely, good to debug

    modelDict = {}
    prog=0.0

    for file in fileList:
        print '  Inspecting file {0}'.format(file)
        print "Progress: %.2f" % (prog/number_of_lines*100) + " %"

        lumis = Lumis(file)
        events = Events(file)
        handle  = Handle('GenFilterInfo')
        label = ('genFilterEfficiencyProducer')
        handleHead = Handle('GenLumiInfoHeader')
        labelHead = ('generator')
        
        for i,lum in enumerate(lumis):

            lum.getByLabel(labelHead,handleHead)
            genHeader = handleHead.product()
            lum.getByLabel(label,handle)
            genFilter = handle.product()
            
            model = genHeader.configDescription()
            modelShort = "_".join(model.split("_")[-2:])

            if not modelShort in modelDict.keys():
                modelDict[modelShort] = {}
                modelDict[modelShort]["pass"] = float(genFilter.numEventsPassed())
                modelDict[modelShort]["total"] = float(genFilter.numEventsTotal())
            else:
                modelDict[modelShort]["pass"] += float(genFilter.numEventsPassed())
                modelDict[modelShort]["total"] += float(genFilter.numEventsTotal())
        prog += 1
      
    oModelDict = OrderedDict(sorted(modelDict.items()))

    print "Total mass points: ",len(oModelDict.keys())

    hFilterEff = r.TH1D('hFilterEff','Gen filter efficiency',len(oModelDict.keys()),0.,float(len(oModelDict.keys())))
    count = 1
    evtsTotAll = 0
    evtsPassAll = 0
    for model,evtsDict in oModelDict.iteritems():
        eff = evtsDict["pass"]/evtsDict["total"]
        evtsTotAll += evtsDict["total"]
        evtsPassAll += evtsDict["pass"]
        # print "{0} {1:.2f}".format(model,eff)
        hFilterEff.GetXaxis().SetBinLabel(count,model)
        hFilterEff.SetBinContent(count,eff)
        count += 1

    print "Average efficiency: {0:.2f}".format(evtsPassAll/evtsTotAll)
    c = r.TCanvas("c","c")
    c.cd()
    hFilterEff.Draw()
    c.SaveAs("FilterEff_"+YEAR+".pdf")
    c.SaveAs("FilterEff_"+YEAR+".png")

    hfile = r.TFile(hfilename, 'RECREATE')

    # Save the effs hist in root format
    # You can later access the effs by: hFilterEff->GetBinContent(hFilterEff->GetXaxis()->FindBin("375_315"))
    hFilterEff.Write()

    return True
    

if __name__ == "__main__": main()
