#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-N2N3_mN-"
JOBS="/afs/cern.ch/work/d/dspitzba/SUSYsignalProduction/GenLHEfiles/GridpackWorkflow/production/SMS-N2N3/jobs"
genprodir="/afs/cern.ch/work/d/dspitzba/SUSYsignalProduction/genproductions/"

#for MNLSP in {100..1300..25} 126 127; do
for MNLSP in 550; do
    python ${SCRIPT} ${MODEL}${MNLSP} --cards-dir ${JOBS}/${MODEL}${MNLSP}  --genproductions-dir ${genprodir}
done
