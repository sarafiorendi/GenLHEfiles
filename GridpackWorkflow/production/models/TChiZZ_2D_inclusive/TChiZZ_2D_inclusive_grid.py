#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "TChiZZ_2D"
process = "N2N3"

# Number of events for mass point, in thousands


# Parameters of 2D scan
xmin, xmax, xstep = 100, 800, 50
ymin, ymax, ystep =   0, 800, 50

# On shell Z
minDiag = 100

# Parameters of extra 1D scan for Higgsino interpretation
d1min, d1max, d1step = 825, 1300, 25

# -------------------------------
#    First the 2D scan

mpoints = []
for mx in range(xmin, xmax+1, xstep):
  for my in range(ymin, ymax+1, ystep):
    if mx-my < minDiag: continue
    if mx <= 400 or (mx > 400 and (mx - my) < 250):
      mpoints.append([mx,my,250])
    else:
      mpoints.append([mx,my,125])


for mx in range(d1min, d1max+1, d1step):
  mpoints.append([mx,1,125])
    
## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Npts, Ndiff = len(mpoints), len(mset)
if Npts==Ndiff: print "\nGrid contains "+str(Npts)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Npts-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

Ntot = makePlot([mpoints], 'events', model, process, xmin, xmax, ymin, ymax)

print '\nScan contains '+"{0:,.0f}".format(Ntot*1000)+" events"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))

print
