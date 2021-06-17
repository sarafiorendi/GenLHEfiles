#!/usr/bin/python
import os, sys
import ROOT as r
r.gROOT.SetBatch(True)
r.PyConfig.IgnoreCommandLineOptions = True
from DataFormats.FWLite import Events, Handle, Lumis
import glob
from collections import OrderedDict

#dasgoclient -query="file dataset=/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM" > T2tt_2017.txt

#fileBase = "/hadoop/cms/store/user/scasasso/mcProduction/AODSIM/T2bW_X05_dM-10to80/T2bW_X05_dM-10to80_genHT-160_genMET-80_{0}.root"
fileBase = "root://cms-xrd-global.cern.ch///store/mc/RunIIAutumn18MiniAOD/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_102X_upgrade2018_realistic_v15-v1/260000/6D0540CE-2D04-3B42-A26B-E8777B3C0924.root"
fileBase = "root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_94X_mc2017_realistic_v15-v1/40000/C01C2B31-CF20-E911-A7A7-48D539D33333.root" 
#fileBase = "root://xrootd-cms.infn.it//store/mc/RunIIFall17MiniAODv2/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_94X_mc2017_realistic_v15-v1/10000/005AD2C8-0D21-E911-9D61-0025905C53F0.root"

YEAR="2017"
YEAR="2018"
hfilename='filterEffs_SMS_T2tt_dM_10to80_genHT_160_genMET_80_mWMin_0p1_'+YEAR+'.root'

def main():

    fileList = []
    samplesFile = open('T2tt_'+YEAR+'.txt')
    samples = samplesFile.readlines()
    for sample in samples:
      fileList += ["root://cms-xrd-global.cern.ch/"+sample.replace('\n', '')]
    #print fileList

    #fileList = [fileBase] #fileList = [fileBase.format(i) for i in range(1,101)]

    modelDict = {}

    for file in fileList:
        print '  Inspecting file {0}'.format(file)

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
    c.SaveAs("FilterEff.pdf")
    c.SaveAs("FilterEff.png")

    hfile = r.TFile(hfilename, 'RECREATE')

    #hfile.cd()
    hFilterEff.Write()
    #hfile.Close()

    return True
    

if __name__ == "__main__": main()
