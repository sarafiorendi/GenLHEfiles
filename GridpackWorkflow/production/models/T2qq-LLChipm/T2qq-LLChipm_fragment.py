import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP2Settings_cfi import *

import math

baseSLHATable="""
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
   1000001     %MSQ%            # ~d_L
   2000001     %MSQ%            # ~d_R
   1000002     %MSQ%            # ~u_L
   2000002     %MSQ%            # ~u_R
   1000003     %MSQ%            # ~s_L
   2000003     %MSQ%            # ~s_R
   1000004     %MSQ%            # ~c_L
   2000004     %MSQ%            # ~c_R
   1000005     1.00000000E+05   # ~b_1
   2000005     1.00000000E+05   # ~b_2
   1000006     1.00000000E+05   # ~t_1
   2000006     1.00000000E+05   # ~t_2
   1000011     1.00000000E+05   # ~e_L
   2000011     1.00000000E+05   # ~e_R
   1000012     1.00000000E+05   # ~nu_eL
   1000013     1.00000000E+05   # ~mu_L
   2000013     1.00000000E+05   # ~mu_R
   1000014     1.00000000E+05   # ~nu_muL
   1000015     1.00000000E+05   # ~tau_1
   2000015     1.00000000E+05   # ~tau_2
   1000016     1.00000000E+05   # ~nu_tauL
   1000021     1.00000000E+05   # ~g
   1000022     %MLSP%           # ~chi_10
   1000023     1.00000000E+05   # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     %MCHI%           # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+

# DECAY TABLE
#         PDG            Width
DECAY   1000001     0.10000000E+00   # sdown_L decays
#          BR         NDA      ID1       ID2
     5.00000000E-01    2     1000022         1
     5.00000000E-01    2          2    -1000024
DECAY   2000001     0.10000000E+00   # sdown_R decays
#          BR         NDA      ID1       ID2
     5.00000000E-01    2     1000022         1
     5.00000000E-01    2          2    -1000024
DECAY   1000002     0.10000000E+00   # sup_L decays
#          BR         NDA      ID1       ID2
     5.00000000E-01    2     1000022         2
     5.00000000E-01    2          1    1000024
DECAY   2000002     0.10000000E+00   # sup_R decays
#          BR         NDA      ID1       ID2
     5.00000000E-01    2     1000022         2
     5.00000000E-01    2          1    1000024
DECAY   1000003     0.10000000E+00   # sstrange_L decays
#          BR         NDA      ID1       ID2
     5.00000000E-01    2     1000022         3
     5.00000000E-01    2          4    -1000024
DECAY   2000003     0.10000000E+00   # sstrange_R decays
#          BR         NDA      ID1       ID2
     5.00000000E-01    2     1000022         3
     5.00000000E-01    2          4    -1000024
DECAY   1000004     0.10000000E+00   # scharm_L decays
#          BR         NDA      ID1       ID2
     5.00000000E-01    2     1000022         4
     5.00000000E-01    2          3    1000024
DECAY   2000004     0.10000000E+00   # scharm_R decays
#          BR         NDA      ID1       ID2
     5.00000000E-01    2     1000022         4
     5.00000000E-01    2          3    1000024
DECAY   1000005     0.00000000E+00   # sbottom1 decays
DECAY   2000005     0.00000000E+00   # sbottom2 decays
DECAY   1000006     0.00000000E+00   # stop1 decays
DECAY   2000006     0.00000000E+00   # stop2 decays

DECAY   1000011     0.00000000E+00   # selectron_L decays
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000012     0.00000000E+00   # snu_elL decays
DECAY   1000013     0.00000000E+00   # smuon_L decays
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000014     0.00000000E+00   # snu_muL decays
DECAY   1000015     0.00000000E+00   # stau_1 decays
DECAY   2000015     0.00000000E+00   # stau_2 decays
DECAY   1000016     0.00000000E+00   # snu_tauL decays
DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023     0.00000000E+00   # neutralino2 decays
DECAY   1000024     %WCHI%           # chargino1 decays 
#    0.00000000E+00    3    1000022    12   -11  # dummy allowed decay, in order to turn on off-shell decays
    1.00000000E+00    2    211	1000022		# x1+  -->  n1 pi+
DECAY   1000025     0.00000000E+00   # neutralino3 decays
DECAY   1000035     0.00000000E+00   # neutralino4 decays
DECAY   1000037     0.00000000E+00   # chargino2+ decays
"""

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)

model = "T2qq-LLChipm_ctau-50"
# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params

ctau =  "10cm"
DeltaM = 0.32485759
ChiWidth = 1.97327052176253113e-15
mcm_eff = 0.222

def matchParams(mass):
    if mass>299 and mass<599: return 62., 0.243
    elif mass<899: return 64., 0.210
    elif mass<1199: return 66., 0.196
    elif mass<1499: return 70., 0.195
    elif mass<1799: return 74., 0.200
    elif mass<2099: return 76., 0.216
    elif mass<2399: return 78., 0.227
    elif mass<2699: return 80., 0.244

#ctau =  "50cm"
#DeltaM = 0.23638902
#ChiWidth = 0.39466403282527335e-15
#mcm_eff = 0.148

#def matchParams(mass):
#    if mass>299 and mass<599: return 62., 0.169
#    elif mass<899: return 64., 0.137
#    elif mass<1199: return 66., 0.127
#    elif mass<1499: return 70., 0.127
#    elif mass<1799: return 74., 0.132
#    elif mass<2099: return 76., 0.137
#    elif mass<2399: return 78., 0.151
#    elif mass<2699: return 80., 0.153

# ctau = "200cm"
#DeltaM = 0.18288376 
#ChiWidth = 0.9866600820631833e-16
#mcm_eff = 0.0713

#def matchParams(mass):
#    if mass>299 and mass<599: return 62., 0.0810
#    elif mass<899: return 64., 0.0657
#    elif mass<1199: return 66., 0.0618
#    elif mass<1499: return 70., 0.0615
#    elif mass<1799: return 74., 0.0649
#    elif mass<2099: return 76., 0.0670
#    elif mass<2399: return 78., 0.0711
#    elif mass<2699: return 80., 0.0792

# Fit to squark cross-section in fb
def xsec(mass):
    if mass < 300: return 319925471928717.38*math.pow(mass, -4.10396285974583*math.exp(mass*0.0001317804474363))
    else: return 6953884830281245*math.pow(mass, -4.7171617288678069*math.exp(mass*6.1752771466190749e-05))

#def matchParams(mass):
#  if mass>99 and mass<199: return 62., 0.498
#  elif mass<299: return 62., 0.361
#  elif mass<399: return 62., 0.302
#  elif mass<499: return 64., 0.275
#  elif mass<599: return 64., 0.254
#  elif mass<1299: return 68., 0.237
#  elif mass<1451: return 70., 0.243
#  elif mass<1801: return 74., 0.246
#  elif mass<2001: return 76., 0.267
#  elif mass<2201: return 78., 0.287
#  elif mass<2601: return 80., 0.320
#  elif mass<2801: return 84., 0.347
#  else: return 84., 0.347 # should not happen

# Parameters that define the grid in the bulk and diagonal
class gridBlock:
  def __init__(self, xmin, xmax, xstep, ystep):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ystep = ystep

# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
goalLumi = 3200
minLumi = 45
minEvents, maxEvents = 20, 250
diagStep = 50
maxDM = 425

scanBlocks = []
scanBlocks.append(gridBlock(300, 2601, 100, 100))
ymin, ymed, ymax = 0, 200, 2200
minDM = 25

# Number of events for mass point, in thousands
def events(mass):
  xs = xsec(mass)
  nev = min(goalLumi*xs, maxEvents*1000)
  if nev < xs*minLumi: nev = xs*minLumi
  nev = max(nev/1000, minEvents)
  return math.ceil(nev) # Rounds up

# -------------------------------
#    Constructing grid

cols = []
Nevents = []
xmin, xmax = 9999, 0
for block in scanBlocks:
  Nbulk, Ndiag = 0, 0
  for mx in range(block.xmin, block.xmax, diagStep):
    xmin = min(xmin, block.xmin)
    xmax = max(xmax, block.xmax)
    col = []
    my = 0
    begDiag = min(max(ymed, mx-maxDM), mx-minDM)
    # Adding bulk points
    if (mx-block.xmin)%block.xstep == 0 :
      for my in range(ymin, begDiag, block.ystep):
        if my > ymax: continue
        nev = events(mx)
        col.append([mx,my, nev])
        Nbulk += nev
    # Adding diagonal points
    for my in range(begDiag, mx-minDM+1, diagStep):
      if my > ymax: continue
      nev = events(mx)
      col.append([mx,my, nev])
      Ndiag += nev
    if(my !=  mx-minDM and mx-minDM <= ymax):
      my = mx-minDM
      nev = events(mx)
      col.append([mx,my, nev])
      Ndiag += nev
    cols.append(col)
  Nevents.append([Nbulk, Ndiag])

mpoints = []
for col in cols: mpoints.extend(col)

for point in mpoints:
    msq, mlsp = point[0], point[1]
    qcut, tru_eff = matchParams(msq)
    wgt = point[2]*(mcm_eff/tru_eff)
    
    if mlsp==0: mlsp = 1
    mchi = mlsp + DeltaM
    slhatable = baseSLHATable.replace('%MSQ%','%e' % msq)
    slhatable = slhatable.replace('%MLSP%','%e' % mlsp)
    slhatable = slhatable.replace('%MCHI%','%e' % mchi)
    slhatable = slhatable.replace('%WCHI%','%e' % ChiWidth)

    basePythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP2SettingsBlock,
        JetMatchingParameters = cms.vstring(
            'JetMatching:setMad = off',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 5.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            'JetMatching:qCut = %.0f' % qcut, #this is the actual merging scale
            'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
            'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
            '6:m0 = 172.5',
            '24:mMin = 0.1',
            'Check:abortIfVeto = on',
        ), 
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP2Settings',
                                    'JetMatchingParameters'
        )
    )

    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(wgt),
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/SMS-SqSq/v1/SMS-SqSq_mSq-%i_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz' % msq),
            ConfigDescription = cms.string('%s_%i_%i_ctau-%s' % (model, msq, mlsp, ctau)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )
