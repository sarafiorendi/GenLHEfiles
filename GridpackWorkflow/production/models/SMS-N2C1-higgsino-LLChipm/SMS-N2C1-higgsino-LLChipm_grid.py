#!/usr/bin/env python

### Script to define scan grid

### Authors:
### Manuel Franco Sevilla
### Ana Ovcharova

import os,sys,math
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from grid_utils import *

model = "SMS-N2C1-higgsino-LLChipm"
process = "Higgsino-N2C1"

mN2s       = [100., 105.,110, 115, 120, 130., 140, 150.,160.,170.,180.,190.,200, 250,300,350, 400,450,500,600,700,800]
nevt       = [5000,4500, 4000,3000,2000,1600,1300,1036,890, 590, 490, 400,  361, 156,  77, 41, 24, 14, 10, 10, 10, 10]
dMs        = [0.25,0.3,0.4,0.5,0.7,1.0,2.0,3.0,4.0,5.0,7.5,10.,13.,16.,20.,30.]
cTauPmMM   = [14096.1052121,5526.98568683,1379.17333781,432.278099693,83.5673365735,19.6905573136,3.75748406136,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05]
WidthPmGEV = [1.39986874964e-17,3.57024575349e-17,1.43076266319e-16,4.56481537973e-16,2.36129305864e-15,1.00214010521e-14,5.25157175805e-14,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08]
cTau20MM   = [8.17342702951,4.75934877833,1.9789196762,1.0115373116,0.342455157649,0.137076872193,0.0288190406857,0.00491725322567,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05,1e-05]
Width20GEV = [2.41425011892e-14,4.14609184934e-14,9.9714492788e-14,1.95076315542e-13,5.76212585423e-13,1.43953512086e-12,6.84710410496e-12,4.01295118889e-11,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08,1.9732697178e-08]

mN1s = []
mC1s = []
# -------------------------------
#    Constructing grid

mpoints = []
for imN2, mN2 in enumerate(mN2s):
  for idM, dM in enumerate(dMs):    
    mN1 = mN2 - dM
    mN1s.append(mN1)
    mC1 = (mN2+mN1)/2.
    mC1s.append(mC1)
    mpoints.append([mN2,mC1,nevt[imN2],Width20GEV[idM],WidthPmGEV[idM]])
    

## Test print out for repeated points
mset = set()
for mp in mpoints: mset.add(mp[0]*10000+mp[1])
Npts, Ndiff = len(mpoints), len(mset)
if Npts==Ndiff: print "\nGrid contains "+str(Npts)+" mass points. No duplicates\n"
else: print "\n\nGRID CONTAINS "+str(Npts-Ndiff)+" DUPLICATE POINTS!!\n\n"

# -------------------------------
#     Plotting and printing

Ntot = makePlot([mpoints], 'events', model, process, mN1s[0], mN1s[-1], mN2s[0], mN2s[-1])

print '\nScan contains '+"{0:.0f}".format(Ntot*1000)+" events"
print 'Average matching efficiency (for McM and GEN fragment) = '+"{0:.3f}".format(getAveEff(mpoints,process))

