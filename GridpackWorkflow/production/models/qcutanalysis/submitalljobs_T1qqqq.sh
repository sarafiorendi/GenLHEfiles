SCRIPT="/afs/cern.ch/work/s/scodella/MonteCarlo/gridtest/GenLHEfiles/GridpackWorkflow/test/scripts/submitLHEPythiaCondorJob.py"
EXECUTABLE=/afs/cern.ch/work/s/scodella/MonteCarlo/gridtest/GenLHEfiles/GridpackWorkflow/production/models/qcutanalysis/runLHEPythiaJob.sh
NJETMAX=2

#PROCESS="T1qqqq-LLChipm_ctau-10"; NJOB=4;
#PROCESS="T1qqqq-LLChipm_ctau-50"; NJOB=7
PROCESS="T1qqqq-LLChipm_ctau-200"; NJOB=12

MODEL="SMS-${PROCESS}_mSq-"
FRAGMENT=/afs/cern.ch/work/s/scodella/MonteCarlo/gridtest/GenLHEfiles/GridpackWorkflow/production/models/qcutanalysis/fragment_LHEGS_${PROCESS}.py
QMIN=125
QMAX=170
QSTP=5

echo $NJOB
echo $FRAGMENT

for MGL in {1000..2801..300}; do
    python $SCRIPT $MODEL$MGL --nevents 5000 --njobs $NJOB --fragment ${FRAGMENT} --qcut-range $QMIN $QMAX --qcut-step $QSTP --nJetMax $NJETMAX --mass $MGL --executable $EXECUTABLE
done
