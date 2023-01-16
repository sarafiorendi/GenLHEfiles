#!/bin/sh
source setup.sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
JOBS="jobs"
PROC="SMS-TStauStau-MM"

for MNLSP in {75..75..1};do
# for MNLSP in {75..75..1} {100..500..50};do
        MODEL=${PROC}"_mStau-"${MNLSP}
        python ${SCRIPT} ${MODEL} --cards-dir ${JOBS}/${MODEL} --genproductions-dir ${genprodir} --proxy ${vomsdir}
    done
done
