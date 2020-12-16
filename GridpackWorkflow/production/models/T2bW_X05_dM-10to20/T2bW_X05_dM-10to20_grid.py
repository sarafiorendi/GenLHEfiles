#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

# Parameters that define the grid in the bulk and diagonal
class gridBlock:
  def __init__(self, xmin, xmax, xstep, ystep):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ystep = ystep
    
model = "T2bW"
process = "StopStop"

# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
goalLumi = 400
minLumi = 50 
minEvents, maxEvents = 40, 1000


# Number of events for mass point, in thousands
def events(mass):
  xs = xsec(mass,process)
  nev = min(goalLumi*xs, maxEvents*1000)
  if nev < xs*minLumi: nev = xs*minLumi
  nev = max(nev/1000, minEvents)
  return math.ceil(nev) # Rounds up

# -------------------------------
#    Constructing grid
#Steps in mStop
xStep, xmin, xmax = 25, 300, 651
ymin, ymax = 0, 1100
#Values of dM(stop, N1)
dMs = [10, 13, 15, 18]

# -------------------------------
#    Constructing grid
mpoints = []
Ndiag = 0
for mx in range(xmin, xmax, xStep):
  for diag in dMs:
    my = mx - diag
    if my > ymax or my < ymin: continue
    nev = events(mx)*2/10 # 2 times as before
    mpoints.append([mx,my, nev])
    Ndiag += nev

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Ntot, Ndiff = len(mpoints), len(mset)
nev_s = "{0:.1f}".format(Ndiag/1000)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points with "+nev_s+"M events. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE MASS POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

makePlot([mpoints], 'events', model, process, xmin, xmax, 0, 100, rotate=True)
Ntot = makePlot([mpoints], 'lumi', model, process, xmin, xmax, ymin, ymax)
Ntot = makePlot([mpoints], 'lumi_br4', model, process, xmin, xmax, ymin, ymax)


print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))
print

