#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-SbotSbot_mSbot-"
JOBS="/afs/cern.ch/work/d/dspitzba/SUSYsignalProduction/GenLHEfiles/GridpackWorkflow/production/SMS-SbotSbot/jobs"
genprodir='/afs/cern.ch/work/d/dspitzba/SUSYsignalProduction/genproductions/'

#for MPROD in {925..1225..50} {1350..1600..50}; do
#for MPROD in {300..1250..25} {1300..2300..50}; do
#for MPROD in {1375..2575..50}; do
for MPROD in {250..275..25}; do
    python ${SCRIPT} ${MODEL}${MPROD} --cards-dir ${JOBS}/${MODEL}${MPROD} --genproductions-dir ${genprodir}
done
