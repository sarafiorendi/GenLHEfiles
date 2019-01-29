import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

import math

baseSLHATable="""
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
   1000001     1.00000000E+05   # ~d_L
   2000001     1.00000000E+05   # ~d_R
   1000002     1.00000000E+05   # ~u_L
   2000002     1.00000000E+05   # ~u_R
   1000003     1.00000000E+05   # ~s_L
   2000003     1.00000000E+05   # ~s_R
   1000004     1.00000000E+05   # ~c_L
   2000004     1.00000000E+05   # ~c_R
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
   1000021     %MGLU%           # ~g
   1000022     1.00000000E+05   # ~chi_10
   1000023     1.00000000E+05   # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     1.00000000E+05   # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+

# DECAY TABLE
#         PDG            Width
DECAY   1000001     0.00000000E+00   # sdown_L decays
DECAY   2000001     0.00000000E+00   # sdown_R decays
DECAY   1000002     0.00000000E+00   # sup_L decays
DECAY   2000002     0.00000000E+00   # sup_R decays
DECAY   1000003     0.00000000E+00   # sstrange_L decays
DECAY   2000003     0.00000000E+00   # sstrange_R decays
DECAY   1000004     0.00000000E+00   # scharm_L decays
DECAY   2000004     0.00000000E+00   # scharm_R decays
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
##### gluino decays - no offshell decays needed
DECAY   1000021     1.00000000E+00   # gluino decays
#           BR         NDA    ID1     ID2     ID3     ID4     ID5
      1.56250000e-02    5      -1       1      11       2      -1 # Lambda_111
      1.56250000e-02    5      -1       1      11       4      -3 # Lambda_122
      1.56250000e-02    5      -1       1      11       2      -3 # Lambda_112
      1.56250000e-02    5      -1       1      11       4      -1 # Lambda_121
      1.56250000e-02    5      -2       2      11       2      -1 # Lambda_111
      1.56250000e-02    5      -2       2      11       4      -3 # Lambda_122
      1.56250000e-02    5      -2       2      11       2      -3 # Lambda_112
      1.56250000e-02    5      -2       2      11       4      -1 # Lambda_121
      1.56250000e-02    5      -3       3      11       2      -1 # Lambda_111
      1.56250000e-02    5      -3       3      11       4      -3 # Lambda_122
      1.56250000e-02    5      -3       3      11       2      -3 # Lambda_112
      1.56250000e-02    5      -3       3      11       4      -1 # Lambda_121
      1.56250000e-02    5      -4       4      11       2      -1 # Lambda_111
      1.56250000e-02    5      -4       4      11       4      -3 # Lambda_122
      1.56250000e-02    5      -4       4      11       2      -3 # Lambda_112
      1.56250000e-02    5      -4       4      11       4      -1 # Lambda_121
      1.56250000e-02    5      -1       1     -11      -2       1 # Lambda_111
      1.56250000e-02    5      -1       1     -11      -4       3 # Lambda_122
      1.56250000e-02    5      -1       1     -11      -2       3 # Lambda_112
      1.56250000e-02    5      -1       1     -11      -4       1 # Lambda_121
      1.56250000e-02    5      -2       2     -11      -2       1 # Lambda_111
      1.56250000e-02    5      -2       2     -11      -4       3 # Lambda_122
      1.56250000e-02    5      -2       2     -11      -2       3 # Lambda_112
      1.56250000e-02    5      -2       2     -11      -4       1 # Lambda_121
      1.56250000e-02    5      -3       3     -11      -2       1 # Lambda_111
      1.56250000e-02    5      -3       3     -11      -4       3 # Lambda_122
      1.56250000e-02    5      -3       3     -11      -2       3 # Lambda_112
      1.56250000e-02    5      -3       3     -11      -4       1 # Lambda_121
      1.56250000e-02    5      -4       4     -11      -2       1 # Lambda_111
      1.56250000e-02    5      -4       4     -11      -4       3 # Lambda_122
      1.56250000e-02    5      -4       4     -11      -2       3 # Lambda_112
      1.56250000e-02    5      -4       4     -11      -4       1 # Lambda_121
      1.56250000e-02    5      -1       1      13       2      -1 # Lambda_211
      1.56250000e-02    5      -1       1      13       4      -3 # Lambda_222
      1.56250000e-02    5      -1       1      13       2      -3 # Lambda_212
      1.56250000e-02    5      -1       1      13       4      -1 # Lambda_221
      1.56250000e-02    5      -2       2      13       2      -1 # Lambda_211
      1.56250000e-02    5      -2       2      13       4      -3 # Lambda_222
      1.56250000e-02    5      -2       2      13       2      -3 # Lambda_212
      1.56250000e-02    5      -2       2      13       4      -1 # Lambda_221
      1.56250000e-02    5      -3       3      13       2      -1 # Lambda_211
      1.56250000e-02    5      -3       3      13       4      -3 # Lambda_222
      1.56250000e-02    5      -3       3      13       2      -3 # Lambda_212
      1.56250000e-02    5      -3       3      13       4      -1 # Lambda_221
      1.56250000e-02    5      -4       4      13       2      -1 # Lambda_211
      1.56250000e-02    5      -4       4      13       4      -3 # Lambda_222
      1.56250000e-02    5      -4       4      13       2      -3 # Lambda_212
      1.56250000e-02    5      -4       4      13       4      -1 # Lambda_221
      1.56250000e-02    5      -1       1     -13      -2       1 # Lambda_211
      1.56250000e-02    5      -1       1     -13      -4       3 # Lambda_222
      1.56250000e-02    5      -1       1     -13      -2       3 # Lambda_212
      1.56250000e-02    5      -1       1     -13      -4       1 # Lambda_221
      1.56250000e-02    5      -2       2     -13      -2       1 # Lambda_211
      1.56250000e-02    5      -2       2     -13      -4       3 # Lambda_222
      1.56250000e-02    5      -2       2     -13      -2       3 # Lambda_212
      1.56250000e-02    5      -2       2     -13      -4       1 # Lambda_221
      1.56250000e-02    5      -3       3     -13      -2       1 # Lambda_211
      1.56250000e-02    5      -3       3     -13      -4       3 # Lambda_222
      1.56250000e-02    5      -3       3     -13      -2       3 # Lambda_212
      1.56250000e-02    5      -3       3     -13      -4       1 # Lambda_221
      1.56250000e-02    5      -4       4     -13      -2       1 # Lambda_211
      1.56250000e-02    5      -4       4     -13      -4       3 # Lambda_222
      1.56250000e-02    5      -4       4     -13      -2       3 # Lambda_212
      1.56250000e-02    5      -4       4     -13      -4       1 # Lambda_221

DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023     0.00000000E+00   # neutralino2 decays
DECAY   1000024     0.00000000E+00   # chargino1+ decays
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

model = "T1qqqqL"
# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params
mcm_eff = 0.253


# Parameters that define the grid in the bulk and diagonal
class gridBlock:
    def __init__(self, xmin, xmax, xstep):
        self.xmin = xmin
        self.xmax = xmax
        self.xstep = xstep 

# Fit to gluino cross-section in fb
def xsec(mass):
    return 4.563e+17*math.pow(mass, -4.761*math.exp(5.848e-05*mass))

def matchParams(mass):
    if   mass<799: return 118., 0.235
    elif mass<999: return 128., 0.235
    elif mass<1199: return 140., 0.235
    elif mass<1399: return 143., 0.245
    elif mass<1499: return 147., 0.255
    elif mass<1799: return 150., 0.267
    elif mass<2099: return 156., 0.290 
    elif mass<2301: return 160., 0.315 
    elif mass<2601: return 162., 0.340
    elif mass<2851: return 168, 0.364 
    else: return 168., 0.315

# Number of events: min(goalLumi*xsec, maxEvents) (always in thousands)
goalLumi = 800
minLumi = 40
minEvents, maxEvents = 20, 150
maxDM = 1000


scanBlocks = []
scanBlocks.append(gridBlock(600,  1200, 100))
scanBlocks.append(gridBlock(1200, 2501, 50)) 

# Number of events for mass point, in thousands
def events(mass):
  xs = xsec(mass)
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

print "Finished grid construction"

for point in mpoints:
    mglu = point[0]
    qcut, tru_eff = matchParams(mglu)
    wgt = point[2]*(mcm_eff/tru_eff)

    slhatable = baseSLHATable.replace('%MGLU%','%e' % mglu) 

    basePythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
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
            'Check:abortIfVeto = on',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'JetMatchingParameters'
        )
    )

    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(wgt),
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/SMS-GlGl/v1/SMS-GlGl_mGl-%i_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz' % mglu),
            ConfigDescription = cms.string('%s_%i' % (model, mglu)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )

