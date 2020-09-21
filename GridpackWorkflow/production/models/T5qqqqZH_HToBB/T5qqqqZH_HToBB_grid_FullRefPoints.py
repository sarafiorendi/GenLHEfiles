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


model   = "T5qqqqZH_HToBB"
process = "GlGl"    
scanBlocksMGlu = []
scanBlocksMGlu.append(gridBlock(1000, 2601, 50))
scanBlocksMN1 = []
scanBlocksMN1.append(gridBlock(0, 1601, 50))
dMGluN1min = 200
dMGluN2    = 50
# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params
nev = 250

# -------------------------------
#    Constructing grid
cols = [[[2200,1,nev]],[[1400,1000,nev]]]
Nevents = [[250,0],[250,0]]
mpoints = []
for col in cols: mpoints.extend(col)
## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]+mp[1]*10000)
Ntot, Ndiff = len(mpoints), len(mset)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

makePlot(cols, 'events', model, process, xmin, xmax, ymin, ymax)
Ntot = makePlot(cols, 'lumi', model, process, xmin, xmax, ymin, ymax)
#makePlot(cols, 'factor')

print '\nScan contains '+"{0:,.0f}".format(Ntot*1.e3)+" events\n"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))
print

print
