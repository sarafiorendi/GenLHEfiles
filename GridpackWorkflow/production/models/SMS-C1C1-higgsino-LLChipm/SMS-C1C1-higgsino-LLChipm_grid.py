#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "SMS-C1C1-higgsino-LLChipm"
process = "C1C1"

xmin, xmax = 100, 800
ymin, ymax = 100, 800
mx_list = [ 100, 110, 120, 130, 150, 180, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800]
ev_list = [2500,2000,1500,1000, 600, 400, 200, 120, 100,  80,  60,  50,  40,  30,  20,  20]
ctau_list = [10, 50, 300]
dmass_list = [0.2, 0.1, 0.05] # Dummy values
width_list = [1.97327052176253113e-15, 0.39466403282527335e-15, 0.9866600820631833e-16] 

# -------------------------------
#    Constructing grid

mpoints = []
for mx in range(len(mx_list)):
    for ct in range(len(ctau_list)):
        mpoints.append([mx_list[mx], mx_list[mx]-dmass_list[ct], float(ev_list[mx]), width_list[ct]]) 
    
## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Npts, Ndiff = len(mpoints), len(mset)
if Npts==Ndiff: print "\nGrid contains "+str(Npts)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Npts-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

Ntot = makePlot([mpoints], 'events', model, process, xmin, xmax, ymin, ymax)

print '\nScan contains '+"{0:.0f}".format(Ntot*1000)+" events"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))

print
