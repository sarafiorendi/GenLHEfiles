#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="SMS-N2N3_mN-"
JOBS="jobs"
genprodir="/home/users/dspitzba/SUSYsignalProduction/genproductions/"

#for MNLSP in {100..1300..25} 126 127; do
for MNLSP in 550; do
    python ${SCRIPT} ${MODEL}${MNLSP} --cards-dir ${JOBS}/${MODEL}${MNLSP}  --genproductions-dir ${genprodir}
done
