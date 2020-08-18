import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

import math

baseSLHATable="""#===================================================================== STAUMIX
Block STAUMIX   # stau mixing matrix
  1  1     1.0   # O_{11}
  1  2     0.0   # O_{12}
  2  1     0.0   # O_{21}
  2  2     1.0   # O_{22}
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
   1000015     %MNLSP%          # ~tau_1
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
BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     1.00000000E+00  # N_11
  1  2     0.00000000E+00  # N_12
  1  3     0.00000000E+00  # N_13
  1  4     0.00000000E+00  # N_14
  2  1     0.00000000E+00  # N_21
  2  2     1.00000000E+00  # N_22
  2  3     0.00000000E+00  # N_23
  2  4     0.00000000E+00  # N_24
  3  1     0.00000000E+00  # N_31
  3  2     0.00000000E+00  # N_32
  3  3     0.70710678E+00  # N_33
  3  4     0.70710678E+00  # N_34
  4  1     0.00000000E+00  # N_41
  4  2     0.00000000E+00  # N_42
  4  3     0.70710678E+00  # N_43
  4  4     -0.70710678E+00  # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1     1.00000000E+00   # U_11
  1  2     0.00000000E+00   # U_12
  2  1     0.00000000E+00   # U_21
  2  2     1.00000000E+00   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1     1.00000000E+00   # V_11
  1  2     0.00000000E+00   # V_12
  2  1     0.00000000E+00   # V_21
  2  2     1.00000000E+00   # V_22
#
BLOCK MSOFT Q=  1.00008208E+04  # The soft SUSY breaking masses at the scale Q
         1     %MN1%            # M_1                 
         2     %MN2%            # M_2                 
         3     1.00000000E+04   # M_3                 
        14    -6.77437438E+02   # A_u                 
        15    -8.59633345E+02   # A_d                 
        16    -2.53493493E+02   # A_e                 
        21     9.86372011E+07   # M^2_Hd              
        22     3.46350951E+06   # M^2_Hu              
        31     1.00000000E+04   # M_eL                
        32     1.00000000E+04   # M_muL               
        33     %MNLSP%          # M_tauL              
        34     1.00000000E+04   # M_eR                
        35     1.00000000E+04   # M_muR               
        36     1.00000000E+04   # M_tauR              
        41     1.00000000E+04   # M_q1L               
        42     1.00000000E+04   # M_q2L               
        43     1.00000000E+04   # M_q3L               
        44     1.00000000E+04   # M_uR                
        45     1.00000000E+04   # M_cR                
        46     1.00000000E+04   # M_tR                
        47     1.00000000E+04   # M_dR                
        48     1.00000000E+04   # M_sR                
        49     1.00000000E+04   # M_bR

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
DECAY   1000024     0.00000000E+00   # neutralino2 decays

#         PDG            Width
DECAY   1000015     1.48327268E-01   # stau_1 decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2     1000022        15   # BR(~tau_1 -> ~chi_10  tau-)
     0.00000000E+00    2     1000023        15   # BR(~tau_1 -> ~chi_20  tau-)
     0.00000000E+00    2     1000025        15   # BR(~tau_1 -> ~chi_30  tau-)
     0.00000000E+00    2     1000035        15   # BR(~tau_1 -> ~chi_40  tau-)
     0.00000000E+00    2    -1000024        16   # BR(~tau_1 -> ~chi_1-  nu_tau)
     0.00000000E+00    2    -1000037        16   # BR(~tau_1 -> ~chi_2-  nu_tau)
     0.00000000E+00    2     1000016       -37   # BR(~tau_1 -> ~nu_tauL H-)
     0.00000000E+00    2     1000016       -24   # BR(~tau_1 -> ~nu_tauL W-)
#

#         PDG            Width
DECAY   1000024     1.70414503E-02   # chargino1+ decays
#          BR         NDA      ID1       ID2
     0.00000000E+00    2     1000002        -1   # BR(~chi_1+ -> ~u_L   db)
     0.00000000E+00    2     2000002        -1   # BR(~chi_1+ -> ~u_R   db)
     0.00000000E+00    2    -1000001         2   # BR(~chi_1+ -> ~d_L*  u )
     0.00000000E+00    2    -2000001         2   # BR(~chi_1+ -> ~d_R*  u )
     0.00000000E+00    2     1000004        -3   # BR(~chi_1+ -> ~c_L   sb)
     0.00000000E+00    2     2000004        -3   # BR(~chi_1+ -> ~c_R   sb)
     0.00000000E+00    2    -1000003         4   # BR(~chi_1+ -> ~s_L*  c )
     0.00000000E+00    2    -2000003         4   # BR(~chi_1+ -> ~s_R*  c )
     0.00000000E+00    2     1000006        -5   # BR(~chi_1+ -> ~t_1   bb)
     0.00000000E+00    2     2000006        -5   # BR(~chi_1+ -> ~t_2   bb)
     0.00000000E+00    2    -1000005         6   # BR(~chi_1+ -> ~b_1*  t )
     0.00000000E+00    2    -2000005         6   # BR(~chi_1+ -> ~b_2*  t )
     0.00000000E+00    2     1000012       -11   # BR(~chi_1+ -> ~nu_eL  e+  )
     0.00000000E+00    2     1000014       -13   # BR(~chi_1+ -> ~nu_muL  mu+ )
     0.00000000E+00    2     1000016       -15   # BR(~chi_1+ -> ~nu_tau1 tau+)
     0.00000000E+00    2    -1000011        12   # BR(~chi_1+ -> ~e_L+    nu_e)
     0.00000000E+00    2    -2000011        12   # BR(~chi_1+ -> ~e_R+    nu_e)
     0.00000000E+00    2    -1000013        14   # BR(~chi_1+ -> ~mu_L+   nu_mu)
     0.00000000E+00    2    -2000013        14   # BR(~chi_1+ -> ~mu_R+   nu_mu)
     0.00000000E+00    2    -1000015        16   # BR(~chi_1+ -> ~tau_1+  nu_tau)
     0.00000000E+00    2    -2000015        16   # BR(~chi_1+ -> ~tau_2+  nu_tau)
     1.00000000E+00    2     1000022        24   # BR(~chi_1+ -> ~chi_10  W+)
     0.00000000E+00    2     1000023        24   # BR(~chi_1+ -> ~chi_20  W+)
     0.00000000E+00    2     1000025        24   # BR(~chi_1+ -> ~chi_30  W+)
     0.00000000E+00    2     1000035        24   # BR(~chi_1+ -> ~chi_40  W+)
     0.00000000E+00    2     1000022        37   # BR(~chi_1+ -> ~chi_10  H+)
     0.00000000E+00    2     1000023        37   # BR(~chi_1+ -> ~chi_20  H+)
     0.00000000E+00    2     1000025        37   # BR(~chi_1+ -> ~chi_30  H+)
     0.00000000E+00    2     1000035        37   # BR(~chi_1+ -> ~chi_40  H+)
#         

#         PDG            Width
DECAY   1000023     2.07770048E-02   # neutralino2 decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2     1000022        23   # BR(~chi_20 -> ~chi_10   Z )
     0.00000000E+00    2     1000024       -24   # BR(~chi_20 -> ~chi_1+   W-)
     0.00000000E+00    2    -1000024        24   # BR(~chi_20 -> ~chi_1-   W+)
     0.00000000E+00    2     1000037       -24   # BR(~chi_20 -> ~chi_2+   W-)
     0.00000000E+00    2    -1000037        24   # BR(~chi_20 -> ~chi_2-   W+)
     0.00000000E+00    2     1000022        25   # BR(~chi_20 -> ~chi_10   h )
     0.00000000E+00    2     1000022        35   # BR(~chi_20 -> ~chi_10   H )
     0.00000000E+00    2     1000022        36   # BR(~chi_20 -> ~chi_10   A )
     0.00000000E+00    2     1000024       -37   # BR(~chi_20 -> ~chi_1+   H-)
     0.00000000E+00    2    -1000024        37   # BR(~chi_20 -> ~chi_1-   H+)
     0.00000000E+00    2     1000037       -37   # BR(~chi_20 -> ~chi_2+   H-)
     0.00000000E+00    2    -1000037        37   # BR(~chi_20 -> ~chi_2-   H+)
     0.00000000E+00    2     1000002        -2   # BR(~chi_20 -> ~u_L      ub)
     0.00000000E+00    2    -1000002         2   # BR(~chi_20 -> ~u_L*     u )
     0.00000000E+00    2     2000002        -2   # BR(~chi_20 -> ~u_R      ub)
     0.00000000E+00    2    -2000002         2   # BR(~chi_20 -> ~u_R*     u )
     0.00000000E+00    2     1000001        -1   # BR(~chi_20 -> ~d_L      db)
     0.00000000E+00    2    -1000001         1   # BR(~chi_20 -> ~d_L*     d )
     0.00000000E+00    2     2000001        -1   # BR(~chi_20 -> ~d_R      db)
     0.00000000E+00    2    -2000001         1   # BR(~chi_20 -> ~d_R*     d )
     0.00000000E+00    2     1000004        -4   # BR(~chi_20 -> ~c_L      cb)
     0.00000000E+00    2    -1000004         4   # BR(~chi_20 -> ~c_L*     c )
     0.00000000E+00    2     2000004        -4   # BR(~chi_20 -> ~c_R      cb)
     0.00000000E+00    2    -2000004         4   # BR(~chi_20 -> ~c_R*     c )
     0.00000000E+00    2     1000003        -3   # BR(~chi_20 -> ~s_L      sb)
     0.00000000E+00    2    -1000003         3   # BR(~chi_20 -> ~s_L*     s )
     0.00000000E+00    2     2000003        -3   # BR(~chi_20 -> ~s_R      sb)
     0.00000000E+00    2    -2000003         3   # BR(~chi_20 -> ~s_R*     s )
     0.00000000E+00    2     1000006        -6   # BR(~chi_20 -> ~t_1      tb)
     0.00000000E+00    2    -1000006         6   # BR(~chi_20 -> ~t_1*     t )
     0.00000000E+00    2     2000006        -6   # BR(~chi_20 -> ~t_2      tb)
     0.00000000E+00    2    -2000006         6   # BR(~chi_20 -> ~t_2*     t )
     0.00000000E+00    2     1000005        -5   # BR(~chi_20 -> ~b_1      bb)
     0.00000000E+00    2    -1000005         5   # BR(~chi_20 -> ~b_1*     b )
     0.00000000E+00    2     2000005        -5   # BR(~chi_20 -> ~b_2      bb)
     0.00000000E+00    2    -2000005         5   # BR(~chi_20 -> ~b_2*     b )
     0.00000000E+00    2     1000011       -11   # BR(~chi_20 -> ~e_L-     e+)
     0.00000000E+00    2    -1000011        11   # BR(~chi_20 -> ~e_L+     e-)
     0.00000000E+00    2     2000011       -11   # BR(~chi_20 -> ~e_R-     e+)
     0.00000000E+00    2    -2000011        11   # BR(~chi_20 -> ~e_R+     e-)
     0.00000000E+00    2     1000013       -13   # BR(~chi_20 -> ~mu_L-    mu+)
     0.00000000E+00    2    -1000013        13   # BR(~chi_20 -> ~mu_L+    mu-)
     0.00000000E+00    2     2000013       -13   # BR(~chi_20 -> ~mu_R-    mu+)
     0.00000000E+00    2    -2000013        13   # BR(~chi_20 -> ~mu_R+    mu-)
     0.00000000E+00    2     1000015       -15   # BR(~chi_20 -> ~tau_1-   tau+)
     0.00000000E+00    2    -1000015        15   # BR(~chi_20 -> ~tau_1+   tau-)
     0.00000000E+00    2     2000015       -15   # BR(~chi_20 -> ~tau_2-   tau+)
     0.00000000E+00    2    -2000015        15   # BR(~chi_20 -> ~tau_2+   tau-)
     0.00000000E+00    2     1000012       -12   # BR(~chi_20 -> ~nu_eL    nu_eb)
     0.00000000E+00    2    -1000012        12   # BR(~chi_20 -> ~nu_eL*   nu_e )
     0.00000000E+00    2     1000014       -14   # BR(~chi_20 -> ~nu_muL   nu_mub)
     0.00000000E+00    2    -1000014        14   # BR(~chi_20 -> ~nu_muL*  nu_mu )
     0.00000000E+00    2     1000016       -16   # BR(~chi_20 -> ~nu_tau1  nu_taub)
     0.00000000E+00    2    -1000016        16   # BR(~chi_20 -> ~nu_tau1* nu_tau )
#
"""

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)
    
model = "VBF_EWKino_WZ"
process = "C1N2"
mcm_eff = 0.536

def matchParams(mass):
    if mass < 124: return 76,0.64
    elif mass < 151: return 76, 0.6
    elif mass < 176: return 76, 0.57
    elif mass < 226: return 76, 0.54
    elif mass < 326: return 76, 0.51
    elif mass < 451: return 76, 0.48
    elif mass < 651: return 76, 0.45
    elif mass < 751: return 76, 0.436
    elif mass < 851: return 76, 0.433
    elif mass < 951: return 76, 0.424
    elif mass < 1051: return 76, 0.421
    elif mass < 1151: return 76, 0.415
    elif mass < 1251: return 76, 0.407
    elif mass < 1351: return 76, 0.400
    elif mass < 1451: return 76, 0.394
    elif mass < 1551: return 76, 0.389
    elif mass < 1651: return 76, 0.384
    elif mass < 1751: return 76, 0.381
    elif mass < 1851: return 76, 0.379
    else: return 76, 0.379

# Parameters that define the grid in the bulk and diagonal
class gridBlock:
  def __init__(self, xmin, xmax, xstep):
    self.xmin = xmin
    self.xmax = xmax
    self.xstep = xstep

scanBlocks = []
scanBlocks.append(gridBlock(100, 401, 25))

deltaM = [ 0.5, 1, 5, 10, 15, 20, 30, 40, 50, 60, 75  ] 

# Number of events for mass point, in thousands
nev = 1000

# -------------------------------
#    Constructing grid

cols = []
Nevents = []
xmin, xmax = 9999, 0
ymin, ymax = 9999, 0
for block in scanBlocks:
  Nbulk, Ndiag = 0, 0
  xmin = min(xmin, block.xmin)
  xmax = max(xmax, block.xmax)
  for mx in range(block.xmin, block.xmax, block.xstep):
    col = []
    for dm in deltaM:
      my = mx-dm
      if my>=0.: 
        ymin = min(ymin, my)
        ymax = max(ymax, my)
        col.append([mx,my,nev])
        Nbulk += nev
    cols.append(col)
  Nevents.append([Nbulk, Ndiag])

mpoints = []
for col in cols: mpoints.extend(col)

for point in mpoints:
    mneu2, mlsp = point[0], point[1]
    qcut, tru_eff = matchParams(mneu2)
    wgt = point[2]*(mcm_eff/tru_eff)
    
    if mlsp==0: mlsp = 1
    mnlsp = (mneu2 + mlsp)/2.
    slhatable = baseSLHATable.replace('%MN2%','%e' % mneu2)
    slhatable = slhatable.replace('%MC1%','%e' % mneu2)
    slhatable = slhatable.replace('%MN1%','%e' % mlsp)
    slhatable = slhatable.replace('%MNLSP%','%e' % mnlsp) 
    
    mlspstr = ( '%.2f' % mlsp).replace('.', 'p')
    
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
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.2/sus_sms/VBF_EWKino/v1/VBF_EWKino_mN2-%i_mN1-%s_tarball.tar.xz' % (mneu2, mlspstr)),
            ConfigDescription = cms.string('%s_%i_%i' % (model, mneu2, mlsp)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )
