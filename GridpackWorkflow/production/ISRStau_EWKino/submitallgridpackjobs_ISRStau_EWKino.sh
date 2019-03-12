#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="ISRStau_EWKino_mN2-"
JOBS="/afs/cern.ch/work/d/dspitzba/SUSYsignalProduction/GenLHEfiles/GridpackWorkflow/production/ISRStau_EWKino/jobs"
genprodir="/afs/cern.ch/work/d/dspitzba/SUSYsignalProduction/genproductions/"

PARTN1="_mN1-"
PARTST="_mStau-"

#ISRStau_EWKino_mN2-%MN2%_mStau-%MNLSP%_mN1-%MN1%

### Create cards and SLHAs for all mass points

for MN2 in 100 150 200 250 300 350 400 450 500; do
#for MN2 in 100; do
  for DM in 50; do
    MN1=`awk "BEGIN {printf \"%.2f\n\", (${MN2}-${DM})}"`
    MNLSP=`awk "BEGIN {printf \"%.2f\n\", ((${MN1}+${MN2})/2)}"`
    MN2STR=${MN2/./p}
    MN1STR=${MN1/./p}
    MC1STR=${MN2/./p}
    MSTSTR=${MNLSP/./p}
    python ${SCRIPT} ${MODEL}${MN2STR}${PARTST}${MSTSTR}${PARTN1}${MN1STR} --cards-dir ${JOBS}/${MODEL}${MN2STR}${PARTST}${MSTSTR}${PARTN1}${MN1STR}  --genproductions-dir ${genprodir}
  done
done


