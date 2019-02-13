SCRIPT="../../test/scripts/submitLHEPythiaCondorJob.py"
MODEL="SMS-StopStop_mStop-"
NJETMAX=2
QMIN=74
QMAX=94
FRAGMENT=fragment_LHEGS.py

for MGL in {2000..2800..100}; do
    python $SCRIPT $MODEL$MGL --nevents 4000 --njobs 5 --fragment ${FRAGMENT} --qcut-range $QMIN $QMAX --qcut-step 2 --nJetMax $NJETMAX --mass $MGL --executable runLHEPythiaJob.sh
done
