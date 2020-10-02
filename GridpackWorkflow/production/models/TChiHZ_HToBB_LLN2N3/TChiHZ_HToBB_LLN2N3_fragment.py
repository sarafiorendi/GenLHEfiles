import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
#from Configuration.Generator.MCTunes2017.PythiaCP2Settings_cfi import *

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
   1000021     1.00000000E+05   # ~g
   1000022     1.00000000E+00   # ~chi_10
   1000023     %MCHI%           # ~chi_20
   1000025     %MCHI%           # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     1.00000000E+05   # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+
   1000039     1.00000000E+05   # ~gravitino

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
DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023     %WCHI%   # neutralino2 decays
    0.00000000E+00    3     1000022   5   -5  # Dummy decay
    0.50000000E+00    2     1000022   25      # BR(N2 -> N1 + H)
    0.500000000E+00   2     1000022   23      # BR(N2 -> N1 + Z)
DECAY   1000024     0.00000000E+00   # chargino1+ decays
DECAY   1000025     %WCHI%   # neutralino3 decays
    0.00000000E+00    3     1000022   5   -5  # Dummy decay 
    0.50000000E+00    2     1000022   25      # BR(N3 -> N1 + H)
    0.500000000E+00   2     1000022   23      # BR(N3 -> N1 + Z)
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

def matchParams(mass):
    if mass < 199: return 76,0.52
    elif mass<299: return 76,0.524
    elif mass<399: return 76,0.492
    elif mass<499: return 76,0.464
    elif mass<599: return 76,0.451
    elif mass<699: return 76,0.437
    elif mass<799: return 76,0.425
    elif mass<899: return 76,0.413
    elif mass<999: return 76,0.402
    elif mass<1099: return 76,0.40
    elif mass<1199: return 76,0.398
    elif mass<1299: return 76,0.394
    elif mass<1451: return 76, 0.388
    elif mass<1651: return 76, 0.389
    elif mass<1851: return 76, 0.382
    else: return 76,0.382

# weighted average of matching efficiencies for the full scan
# must equal the number entered in McM generator params
mcm_eff = 0.503

model = "TChiHZ_HToBB_LLN2N3"
process = "N2N3"

#Need hbar*c to convert lifetime to width    
hBarCinGeVmm = 1.973269788e-13

#Scan parameters
mchi  = [127.,150.,175.,200.,250.,300.,400.,600.,800.,1000.,1250.,1500.,1800.]
nevs  = [600.,500.,350.,250.,150.,100., 50., 50., 50.,  50.,  50.,  50.,  50.] #Weight more higher x-sec regions as requested per analysts
totevents = sum(nevs)
ctauValues = [500,3000] # Neutralino lifetime in mm
wchi  = [ hBarCinGeVmm/ctau0 for ctau0 in ctauValues ]

mpoints = []
for i, m in enumerate(mchi):
  for w in wchi:
    mpoints.append([m,w,nevs[i]])

for point in mpoints:
    mchi, wchi, nevents = point[0], point[1], point[2]
    tchi  = hBarCinGeVmm/wchi 
    qcut, tru_eff = matchParams(mchi)
    wgt = point[2]*(mcm_eff/tru_eff)

    slhatable = baseSLHATable.replace('%MCHI%','%e' % mchi)
    slhatable = slhatable.replace('%WCHI%','%e' % wchi)

    basePythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        #pythia8CP2SettingsBlock,
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
            '25:onMode = off',
            '25:onIfMatch = 5 -5', # Only H->bb decays
            '25:m0 = 125.0',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    #'pythia8CP2Settings',
                                    'JetMatchingParameters'
        )
    )

    for p in [1000023, 1000025]: # Fix N2/N3 lifetimes
        basePythiaParameters.pythia8CommonSettings.extend([str(p)+':tau0 = %e' % hBarCinGeVmm/wchi]) # Pythia8 should compute it from the width, but let's be safe here
    basePythiaParameters.pythia8CommonSettings.extend(['LesHouches:setLifetime = 2'])                # Override gridpack's infinite lifetimes for N2/N3, lets pythia lifetimes take preference

    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(wgt),
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/SMS-%s/v1/SMS-%s_mN-%i_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz' % (process,process,mchi)),
            ConfigDescription = cms.string('%s_%i_%i' % (model, mchi, tchi)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )

