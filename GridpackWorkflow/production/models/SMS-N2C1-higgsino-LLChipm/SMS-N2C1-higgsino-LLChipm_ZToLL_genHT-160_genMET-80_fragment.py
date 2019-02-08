import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

#import scipy.constants as scc
#def convertCTauInM_To_WidthInGeV(ctau):
#    return scc.physical_constants["Planck constant over 2 pi in eV s"][0]*1.e-9*scc.c/ctau
    
import math

baseSLHATable="""
#
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
        35     1.00000000E+05
        36     1.00000000E+05
        37     1.00000000E+05
        6      1.72500000E+02
   1000001     1.00000000E+05    # ~d_L
   2000001     1.00000000E+05   # ~d_R
   1000002     1.00000000E+05    # ~u_L
   2000002     1.00000000E+05   # ~u_R
   1000003     1.00000000E+05    # ~s_L
   2000003     1.00000000E+05   # ~s_R
   1000004     1.00000000E+05    # ~c_L
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
   1000021     1.00000000E+05   # ~g
   1000022     %MN1%            # ~chi_10
   1000023     %MN2%            # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     %MC1%            # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+
#
#
#
#         PDG            Width
DECAY         6     1.134E+00        # top decays
DECAY   2000006     0.00000000E+00   # stop2 decays
DECAY   1000005     0.00000000E+00   # sbottom1 decays
DECAY   2000005     0.00000000E+00   # sbottom2 decays
#
#         PDG            Width
DECAY   1000011     0.00000000E+00   # selectron_L decays
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000013     0.00000000E+00   # smuon_L decays
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000015     0.00000000E+00   # stau_1 decays
DECAY   2000015     0.00000000E+00   # stau_2 decays
#
#         PDG            Width
DECAY   1000012     0.00000000E+00   # snu_elL decays
DECAY   1000014     0.00000000E+00   # snu_muL decays
DECAY   1000016     0.00000000E+00   # snu_tauL decays
DECAY   1000006     0.00000000E+00   # stop1 decays
DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023     %WIDTH0%   # neutralino2 decays # taken from TChiWZ_ZToLL
    0.00000000E+00   3    1000022   11   -11
    1.00000000E+00   2    1000022   23
#    0.3334E+00         3    1000022   11   -11  # neutralino2 decays
#    0.3334E+00         3    1000022   13   -13  # neutralino2 decays
#    0.3332E+00         3    1000022   15   -15  # neutralino2 decays
DECAY   1000024     %WIDTHpm%   # chargino1+ decays # taken from T2bW_X05_dM-10to80 (or better https://github.com/CMS-SUS-XPAG/GenLHEfiles/blob/master/GridpackWorkflow/production/models/T2bt/T2bt_fragment.py#L71-80 ?) 
    0.00000000E+00    3    1000022     -1    2  # dummy allowed decay, in order to turn on off-shell decays
    1.00000000E+00    2    1000022      24
#    1.00000000E+00    3    1000022      -11   12
"""

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)

def matchParams(mass):
  if mass < 101.: return 76,0.644
  elif mass < 121.: return 76,0.622
  elif mass < 141.: return 76,0.600
  elif mass < 161.: return 76,0.584
  elif mass < 181.: return 76,0.570
  elif mass < 201.: return 76,0.555
  elif mass < 221.: return 76,0.543
  elif mass < 241.: return 76,0.533
  else: return 76,0.5 # it shouldn't be used anyway

model = "SMS-N2C1-higgsino-LLChipm"
process = "Higgsino-N2C1"

# Number of events for mass point, in thousands
#nevt = 100

# -------------------------------
#    Constructing grid
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
    

for point in mpoints:

    mn2, mc1, wn2, wc1 = point[0], point[1], point[3], point[4]
    #dM = 2*(mn2-mc1)
    #mn1 = mn2 - dM
    #mc1 = (mn2+mn1)/2.
    mn1 = 2.*mc1 - mn2

    mn2Str = str(int(mn2))
    #mn1Str = "{0:.2f}".format(mn1).replace(".","p")
    mc1Str = "{0:.2f}".format(mc1).replace(".","p")

    qcut, tru_eff = matchParams(mn2)
    wgt = point[2]/tru_eff
    
    slhatable = baseSLHATable.replace('%MN2%','%e' % mn2)
    slhatable = slhatable.replace('%MC1%','%e' % mc1)
    slhatable = slhatable.replace('%MN1%','%e' % mn1)
    
    slhatable = slhatable.replace('%WIDTH0%','%e' % wn2)
    slhatable = slhatable.replace('%WIDTHpm%','%e' % wc1)    

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
            '23:onMode = off',
            '23:onIfAny = 11 13 15',
            '24:mMin = 0.01',
            '23:mMin = 0.01',
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
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/%s/v1/%s_mN2-%s_mC1-%s_tarball.tar.xz' % (process,process,mn2Str,mc1Str)),
            ConfigDescription = cms.string('%s_%s_%s' % (model, mn2Str,mc1Str)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )


#     Filter setup
# ------------------------
# https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_X/PhysicsTools/HepMCCandAlgos/python/genParticles_cfi.py
tmpGenParticles = cms.EDProducer("GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator","unsmeared"),
    abortOnUnknownPDGCode = cms.untracked.bool(False)
)

# https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_X/RecoJets/Configuration/python/GenJetParticles_cff.py
# https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_X/RecoMET/Configuration/python/GenMETParticles_cff.py
tmpGenParticlesForJetsNoNu = cms.EDProducer("InputGenJetsParticleSelector",
    src = cms.InputTag("tmpGenParticles"),
    ignoreParticleIDs = cms.vuint32(
         1000022, 1000023, 1000024,
         1000012, 1000014, 1000016,
         2000012, 2000014, 2000016,
         1000039, 5100039,
         4000012, 4000014, 4000016,
         9900012, 9900014, 9900016,
         39,12,14,16),
    partonicFinalState = cms.bool(False),
    excludeResonances = cms.bool(False),
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    tausAsJets = cms.bool(False)
)

# https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_X/RecoJets/JetProducers/python/AnomalousCellParameters_cfi.py
AnomalousCellParameters = cms.PSet(
    maxBadEcalCells         = cms.uint32(9999999),
    maxRecoveredEcalCells   = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxBadHcalCells         = cms.uint32(9999999),
    maxRecoveredHcalCells   = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999)
)

# https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_X/RecoJets/JetProducers/python/GenJetParameters_cfi.py
GenJetParameters = cms.PSet(
    src            = cms.InputTag("tmpGenParticlesForJetsNoNu"),
    srcPVs         = cms.InputTag(''),
    jetType        = cms.string('GenJet'),
    jetPtMin       = cms.double(3.0),
    inputEtMin     = cms.double(0.0),
    inputEMin      = cms.double(0.0),
    doPVCorrection = cms.bool(False),
    # pileup with offset correction
    doPUOffsetCorr = cms.bool(False),
       # if pileup is false, these are not read:
       nSigmaPU = cms.double(1.0),
       radiusPU = cms.double(0.5),
    # fastjet-style pileup
    doAreaFastjet  = cms.bool(False),
    doRhoFastjet   = cms.bool(False),
      # if doPU is false, these are not read:
      Active_Area_Repeats = cms.int32(5),
      GhostArea = cms.double(0.01),
      Ghost_EtaMax = cms.double(6.0),
    Rho_EtaMax = cms.double(4.5),
    useDeterministicSeed= cms.bool( True ),
    minSeed             = cms.uint32( 14327 )
)


# https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_X/RecoJets/JetProducers/python/ak4GenJets_cfi.py
tmpAk4GenJetsNoNu = cms.EDProducer(
    "FastjetJetProducer",
    GenJetParameters,
    AnomalousCellParameters,
    jetAlgorithm = cms.string("AntiKt"),
    rParam       = cms.double(0.4)
)

genHTFilter = cms.EDFilter("GenHTFilter",
   src = cms.InputTag("tmpAk4GenJetsNoNu"), #GenJet collection as input
   jetPtCut = cms.double(30.0), #GenJet pT cut for HT
   jetEtaCut = cms.double(5.0), #GenJet eta cut for HT
   genHTcut = cms.double(160.0) #genHT cut
)


tmpGenMetTrue = cms.EDProducer("GenMETProducer",
    src = cms.InputTag("tmpGenParticlesForJetsNoNu"),
    onlyFiducialParticles = cms.bool(False), ## Use only fiducial GenParticles
    globalThreshold = cms.double(0.0), ## Global Threshold for input objects
    usePt   = cms.bool(True), ## using Pt instead Et
    applyFiducialThresholdForFractions   = cms.bool(False),
)

genMETfilter1 = cms.EDFilter("CandViewSelector",
   src = cms.InputTag("tmpGenMetTrue"),
   cut = cms.string("pt > 80")
)

genMETfilter2 = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("genMETfilter1"),
    minNumber = cms.uint32(1),
)


ProductionFilterSequence = cms.Sequence(generator*
                                        tmpGenParticles * tmpGenParticlesForJetsNoNu *
                                        tmpAk4GenJetsNoNu * genHTFilter *
                                        tmpGenMetTrue * genMETfilter1 * genMETfilter2
)
