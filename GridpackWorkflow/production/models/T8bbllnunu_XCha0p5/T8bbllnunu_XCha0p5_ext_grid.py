#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *
import pprint

model = "T8bbllnunu_XCha0p5"
process = "StopStop"

period = "Summer16"

# Number of events for mass point, in thousands
nevt = 50

diag_low, diag_high = 100, 100
xmin, xmax, xstep = 200, 1800, 50
ymin, ymax, ystep_low, ystep_high = 700, 1600, 50, 50

# -------------------------------
#    Constructing grid

mTot = 0
mpoints = []
for mx in range(xmin, xmax+1, xstep):
  ylist = []
  if mx > (ymax + (diag_low - diag_high)):
    ylist.extend(range(ymin, ymax+1, ystep_low))
  elif mx > ymax:
    ylist.extend(range(ymin, mx - diag_low, ystep_low))
    ylist.extend(range(mx - diag_low, ymax+1, ystep_high))
  else:
    ylist.extend(range(ymin, mx - diag_low, ystep_low))
    ylist.extend(range(mx - diag_low, mx-diag_high+1, ystep_high))
  for my in ylist:
    mTot += nevt
    mpoints.append([mx,my,nevt])

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Ntot, Ndiff = len(mpoints), len(mset)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing
print 1000*mTot, 'events'
"""
makePlot(cols, 'events', model, process, xmin, xmax, ymin, ymax)
Ntot = makePlot(cols, 'lumi', model, process, xmin, xmax, ymin, ymax)


Ntot = Ntot/1e3
print '\nScan contains '+"{0:.0f}".format(Ntot*1e6)+" events\n"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))
print

for ind in range(len(scanBlocks)):
  Nbulk, Ndiag = Nevents[ind][0]/1e3, Nevents[ind][1]/1e3
  Nblock = Nbulk+Ndiag
  print "From "+'{:>4}'.format(scanBlocks[ind].xmin)+" to "+str(scanBlocks[ind].xmax)+": ",
  print "{0:>4.1f}".format(Nblock)+"M ("+"{0:>4.1f}".format(Nblock/Ntot*100)+" %) events, "+"{0:>4.1f}".format(Nbulk),
  print "M ("+"{0:>4.1f}".format(Nbulk/Ntot*100)+" %) in the bulk, "+"{0:>4.1f}".format(Ndiag)+"M (",
  print "{0:.1f}".format(Ndiag/Ntot*100)+" %) in the diagonal"

print
"""
