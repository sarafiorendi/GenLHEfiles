SCRIPT="/afs/cern.ch/work/s/scodella/MonteCarlo/gridtest/GenLHEfiles/GridpackWorkflow/test/scripts/submitLHEPythiaCondorJob.py"
MODEL="SMS-T2qq-LLChipm_ctau-200_mSq-"
NJETMAX=2
QMIN=80
QMAX=80
FRAGMENT=/afs/cern.ch/work/s/scodella/MonteCarlo/gridtest/GenLHEfiles/GridpackWorkflow/production/models/qcutanalysis/fragment_LHEGS_T2qq-LLChipm_ctau-200.py
EXECUTABLE=/afs/cern.ch/work/s/scodella/MonteCarlo/gridtest/GenLHEfiles/GridpackWorkflow/production/models/qcutanalysis/runLHEPythiaJob.sh

for MGL in {2000..2001..100}; do
    python $SCRIPT $MODEL$MGL --nevents 100 --njobs 5 --fragment ${FRAGMENT} --qcut-range $QMIN $QMAX --qcut-step 2 --nJetMax $NJETMAX --mass $MGL --executable $EXECUTABLE
done
