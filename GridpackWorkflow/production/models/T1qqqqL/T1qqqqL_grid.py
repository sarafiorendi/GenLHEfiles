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
    def __init__(self, xmin, xmax, xstep):
        self.xmin = xmin
        self.xmax = xmax
        self.xstep = xstep 


model = "T1qqqqL"
process = "GlGl"

period = "Fall17"

# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
goalLumi = 800
minLumi = 40
minEvents, maxEvents = 50, 150
maxDM = 1000
ymin, ymax = 0, 10 # for the plot

if period == "Fall17" :
    minLumi = 45
    minEvents = 55

scanBlocks = []
scanBlocks.append(gridBlock(600,  1200, 100))
scanBlocks.append(gridBlock(1200, 2501, 50)) 

# Number of events for mass point, in thousands
def events(mass):
  xs = xsec(mass, process)
  nev = min(goalLumi*xs, maxEvents*1000)
  if nev < xs*minLumi: nev = xs*minLumi
  nev = max(nev/1000, minEvents)
  return math.ceil(nev) # Rounds up

#    Constructing grid

print "Starting grid construction"

cols = []
Nevents = []
xmin, xmax = 9999, 0
for block in scanBlocks:
  Nbulk, Ndiag = 0, 0
  for mx in range(block.xmin, block.xmax):
    xmin = min(xmin, block.xmin)
    xmax = max(xmax, block.xmax)
    col = [] 
    if (mx-block.xmin)%block.xstep == 0 : 
        nev = events(mx)
        col.append([mx,1,nev])
        Nbulk += nev 
    cols.append(col)
  Nevents.append([Nbulk, Ndiag])

mpoints = []
for col in cols: mpoints.extend(col)

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Ntot, Ndiff = len(mpoints), len(mset)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

makePlot(cols, 'events', model, process, xmin, xmax, ymin, ymax)
Ntot = makePlot(cols, 'lumi', model, process, xmin, xmax, ymin, ymax)
#makePlot(cols, 'factor')

Ntot = Ntot/1e3
print '\nScan contains '+"{0:.6f}".format(Ntot)+" million events\n"
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
