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


model   = "TChiHZ"
process = "N2N3"    

#Need hbar*c to convert lifetime to width
hBarCinGeVmm = 1.973269788e-13

xmin = 100
xmax = 2000
ymin = 0 
ymax = 4500
#Scan parameters
mchi  = [127.,150.,175.,200.,250.,300.,400.,600.,800.,1000.,1250.,1500.,1800.]
nevs  = [600.,500.,350.,250.,150.,100., 50., 50., 50.,  50.,  50.,  50.,  50.] #Weight more higher x-sec regions
ctauValues = [500,3000] # Neutralino lifetime in mm
wchi  = [ hBarCinGeVmm/ctau0 for ctau0 in ctauValues ]

mpoints = []
for i, m in enumerate(mchi):
  for w in ctauValues: #Just so we don't mess with something unreadable
    mpoints.append([m,w,nevs[i]])
cols = [mpoints]

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]+mp[1]*10000)
Ntot, Ndiff = len(mpoints), len(mset)
if Ntot==Ndiff: print "\nGrid contains "+str(Ntot)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Ntot-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

makePlot(cols, 'events', model, process, xmin, xmax, ymin, ymax, ylabel="$c\\tau [mm]$")
Ntot = makePlot(cols, 'lumi', model, process, xmin, xmax, ymin, ymax)
#makePlot(cols, 'factor')

print '\nScan contains '+"{0:,.0f}".format(Ntot*1.e3)+" events\n"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))
print

print
