import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

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
   2000005     1.10000000E+05   # ~b_2
   1000006     1.10000000E+05   # ~t_1
   2000006     1.10000000E+05   # ~t_2
   1000011     %MSLEP%          # ~e_L
   2000011     %MSLEP%          # ~e_R
   1000012     1.00000000E+05   # ~nu_eL
   1000013     %MSLEP%          # ~mu_L
   2000013     %MSLEP%          # ~mu_R
   1000014     1.00000000E+05   # ~nu_muL
   1000015     1.00000000E+05   # ~tau_1
   2000015     1.00000000E+05   # ~tau_2
   1000016     1.00000000E+05   # ~nu_tauL
   1000021     1.00000000E+05   # ~g
   1000022     100              # ~chi_10
   1000023     %MCHI2%          # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     1.00000000E+05   # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+
#
#
#
# DECAY TABLE
#         PDG            Width
DECAY   1000006     0.00000000E+00   # stop1 decays
DECAY   2000006     0.00000000E+00   # stop2 decays
DECAY   1000005     0.00000000E+00   # sbottom1 decays
DECAY   2000005     0.00000000E+00   # sbottom2 decays
#
#         PDG            Width
DECAY   1000011 2.00000000E-02        # selectron_L decays
 1.00000000E+00 2 1000022 11          # BR( selectron_L -> ~chi_10 e-)
DECAY   2000011 2.00000000E-02        # selectron_R decays
 1.00000000E+00 2 1000022 11          # BR( selectron_R -> ~chi_10 e-)
DECAY   1000013 2.00000000E-02        # smuon_L decays
 1.00000000E+00 2 1000022 13          # BR( smuon_L -> ~chi_10 mu-)
DECAY   2000013 2.00000000E-02        # smuon_R decays
 1.00000000E+00 2 1000022 13          # BR( smuon_L -> ~chi_10 mu-)
DECAY   1000015     0.00000000E+00   # stau_1 decays
DECAY   2000015     0.00000000E+00   # stau_2 decays
#
#         PDG            Width
DECAY   1000012     0.00000000E+00   # snu_elL decays
DECAY   1000014     0.00000000E+00   # snu_muL decays
DECAY   1000016     0.00000000E+00   # snu_tauL decays

#         PDG            Width
DECAY   1000001     3.00000000E+00   # sdown_L decays
 1.00000E+00    2     1000023         1
DECAY   2000001     3.00000000E+00   # sdown_R decays
 1.00000E+00    2     1000023         1
DECAY   1000002     3.00000000E+00   # sup_L decays
 1.00000E+00    2     1000023         2
DECAY   2000002     3.00000000E+00   # sup_R decays
 1.00000E+00    2     1000023         2
DECAY   1000003     3.00000000E+00   # sstrange_L decays
 1.00000E+00    2     1000023         3
DECAY   2000003     3.00000000E+00   # sstrange_R decays
 1.00000E+00    2     1000023         3
DECAY   1000004     3.00000000E+00   # scharm_L decays
 1.00000E+00    2     1000023         4
DECAY   2000004     3.00000000E+00   # scharm_R decays
 1.00000E+00    2     1000023         4

DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023 2.00000000E-02        # neutralino2 decays
 5.00000000E-01 2 1000022  23         # BR(~chi_20 -> ~chi_10 d db)
 1.25000000E-01 2 1000011 -11         # BR(~chi_20 -> selectron_L e+)
 1.25000000E-01 2 2000011 -11         # BR(~chi_20 -> selectron_R e+)
 1.25000000E-01 2 1000013 -13         # BR(~chi_20 -> smuon_L mu+)
 1.25000000E-01 2 2000013 -13         # BR(~chi_20 -> smuon_R mu+)
"""

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)

model = "T6qqllslepton"

def matchParams(mass):
    if mass>99 and mass<199: return 62., 0.498
    elif mass<299: return 62., 0.361
    elif mass<399: return 62., 0.302
    elif mass<499: return 64., 0.275
    elif mass<599: return 64., 0.254
    elif mass<1299: return 68., 0.237
    elif mass<1451: return 70., 0.243
    elif mass<1801: return 74., 0.246
    elif mass<2001: return 76., 0.267
    elif mass<2201: return 78., 0.287
    elif mass<2601: return 80., 0.320
    elif mass<2801: return 84., 0.347 
    else: return 84., 0.347

# Parameters that define the grid in the bulk and diagonal
class gridBlock:
  def __init__(self, xmin, xmax, xstep, ystep, diagStep, minEvents):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep
    self.ystep = ystep
    self.diagStep = diagStep
    self.minEvents = minEvents
    
nevt = 50

scanBlocks = []

scanBlocks.append(gridBlock(1000, 2101, 50, 50, 50,50))
minDM = 50
maxDM = 300
ymin, ymed, ymax = 150, 150, 2100
hlines_below_grid = []
hline_xmin = 400

# -------------------------------
#    Constructing grid

cols = []
Nevents = []
xmin, xmax = 9999, 0
for block in scanBlocks:
  Nbulk, Ndiag = 0, 0
  minEvents = block.minEvents
  for mx in range(block.xmin, block.xmax, block.diagStep):
    xmin = min(xmin, block.xmin)
    xmax = max(xmax, block.xmax)
    col = []
    my = 0
    begDiag = max(ymed, mx-maxDM)
    # Adding bulk points
    if (mx-block.xmin)%block.xstep == 0:
      # adding extra horizontal lines
      yrange = []
      if (mx>=hline_xmin): yrange.extend(hlines_below_grid)
      else: yrange.append(hlines_below_grid[0])
      yrange.extend(range(ymin, begDiag, block.ystep))
      for my in yrange:
        if my > ymax: continue
        nev = nevt
        col.append([mx,my, nev])
        Nbulk += nev
    # Adding diagonal points
    for my in range(begDiag, mx-minDM+1, block.diagStep):
      if my > ymax: continue
      nev = nevt
      col.append([mx,my, nev])
      Ndiag += nev
    if(my !=  mx-minDM and mx-minDM <= ymax):
      my = mx-minDM
      nev = nevt
      col.append([mx,my, nev])
      Ndiag += nev
    cols.append(col)
  Nevents.append([Nbulk, Ndiag])

mpoints = []
for col in cols: mpoints.extend(col)

for point in mpoints:
    msq, mchi2 = point[0], point[1]
    mslep = (mchi2+100)/2.
    qcut, tru_eff = matchParams(msq)
    wgt = point[2]/tru_eff
    
    slhatable = baseSLHATable.replace('%MSQ%','%e' % msq)
    slhatable = slhatable.replace('%MCHI2%','%e' % mchi2)
    slhatable = slhatable.replace('%MSLEP%','%e' % mslep)

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
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/SMS-SqSq/v1/SMS-SqSq_mSq-%i_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz' % msq),
            ConfigDescription = cms.string('%s_%i_%i' % (model, msq, mchi2)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )
