#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "TStauStau-SoftLH"
process = "StauStau-LH"

xmin, xmax = 0, 500
ymin, ymax = 0, 500

mstaus = [100,150,200,250,300,350,400]
dmass = [10,20,30,40,50]

# Number of events in thousands per mass point
def events(mx,my):
    return 100

# -------------------------------
#    Constructing grid

mpoints = []

for mx in mstaus:
    for dm in dmass:
        my = mx - dm
        mpoints.append([mx,my,events(mx,my)])

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Npts, Ndiff = len(mpoints), len(mset)
if Npts==Ndiff: print "\nGrid contains "+str(Npts)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Npts-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

Ntot = makePlot([mpoints], 'events', model, process, xmin, xmax, ymin, ymax)

print '\nScan contains '+"{0:.3f}".format(Ntot*1000)+" events"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))

print
