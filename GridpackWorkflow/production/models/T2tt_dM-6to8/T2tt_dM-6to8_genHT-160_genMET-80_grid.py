#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "T2tt_dM-6to8_genHT-160_genMET-80"
process = "StopStop"

period = "Summer16"

# -------------------------------
#    Constructing grid

mpoints = []
nev=250
def GetAllStopNeutralinoPoints(minStop = 300, maxStop = 1000, dStop = 100, mindif = 6, maxdif = 8, ddif = 2):
  points = []
  for mStop in range(minStop, maxStop+dStop, dStop):
    for dif in range(mindif, maxdif+ddif, ddif):
      mChi = mStop-dif
      points.append([mStop, mChi,nev])
  return points
mpoints=GetAllStopNeutralinoPoints()

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Ntot, Ndiff = len(mpoints), len(mset)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing
xmin, xmax, xstep = 300, 1000, 100
ymin, ymax, ystep = 292, 994, 100

makePlot([mpoints], 'events', model, process, xmin, xmax, ymin, ymax)

print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))
print

