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
    
model = "T2tt_4bd"
process = "StopStop"

period = "Summer16"

# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
goalLumi = 400
if "16" in period : minLumi = 50
elif "17" in period : minLumi = 57   
minEvents, maxEvents = 50, 1000
xdiagStep, ydiagStep = 25, 10
minDM, maxDM = 10, 80

scanBlocks = []
if period == "Spring16" : 
  scanBlocks.append(gridBlock(250,  801, 25, 10)) #Using only [x,y]diagStep
  ymin, ymax = 0, 1100 
elif (period == "Summer16" or period == "Fall17") : 
  scanBlocks.append(gridBlock(250,  1101, 25, 10)) #Using only [x,y]diagStep
  ymin, ymax = 0, 1400

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
ymin, ymax = 200, 1100
#Values of dM(stop, N1)
dMs = [10, 13, 15, 18, 20]

# -------------------------------
#    Constructing grid
Ndiag = 0
mpoints = []
for mx in range(xmin, xmax, xStep):
  for diag in dMs:
    my = mx - diag
    if my > ymax or my < ymin: continue
    nev = events(mx)*(2 - (dMs==20))/10. # A nasty trick, we need less stats for dM=20 GeV as it already exists in previous scans but analysts want it anyway for cross-checking
    mpoints.append([mx,my, nev])
    Ndiag += nev

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Ntot, Ndiff = len(mpoints), len(mset)
nev_s = "{0:.3f}".format(Ndiag/1000)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points with "+nev_s+"M events. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE MASS POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

makePlot([mpoints], 'events', model, process, xmin, xmax, 0, 100, rotate=True)
Ntot = makePlot([mpoints], 'lumi', model, process, xmin, xmax, ymin, ymax)
Ntot = makePlot([mpoints], 'lumi_br4', model, process, xmin, xmax, ymin, ymax)


print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))
print

