# Compute signal trigger efficiencies for 2017 and 2018 Legacy dataset

As a wise man once said: _Messy but quicker._

Get the sample file name in txt format for 2017:

```
dasgoclient -query="file dataset=/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15-v1/MINIAODSIM" > T2tt_2017_1.txt

dasgoclient -query="file dataset=/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_94X_mc2017_realistic_v15_ext1-v1/MINIAODSIM" > T2tt_2017_2.txt

cat T2tt_2017_1.txt T2tt_2017_2.txt > T2tt_2017.txt
```

For 2018:

```
dasgoclient -query="file dataset=/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_102X_upgrade2018_realistic_v15-v1/MINIAODSIM" > T2tt_2018.txt
```

Later, in your analysis sample processing scrip access the efficiency by (ex.) `hFilterEff->GetBinContent(hFilterEff->GetXaxis()->FindBin("375_315"))`
