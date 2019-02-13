SCRIPT="/afs/cern.ch/work/d/dspitzba/SUSYsignalProduction/GenLHEfiles/GridpackWorkflow/test/scripts/submitLHEPythiaCondorJob.py"
MODEL="SMS-StopStop_mStop-"
NJETMAX=2
QMIN=80
QMAX=80
FRAGMENT=/afs/cern.ch/work/d/dspitzba/SUSYsignalProduction/GenLHEfiles/GridpackWorkflow/production/SMS-StopStop/fragment_LHEGS.py
EXECUTABLE=/afs/cern.ch/work/d/dspitzba/SUSYsignalProduction/GenLHEfiles/GridpackWorkflow/production/SMS-StopStop/runLHEPythiaJob.sh

for MGL in {2000..2001..100}; do
    python $SCRIPT $MODEL$MGL --nevents 100 --njobs 5 --fragment ${FRAGMENT} --qcut-range $QMIN $QMAX --qcut-step 2 --nJetMax $NJETMAX --mass $MGL --executable $EXECUTABLE
done
