#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob.py"
MODEL="ISRStau_DirectStau_mStau-"
JOBS="/afs/cern.ch/work/d/dspitzba/SUSYsignalProduction/GenLHEfiles/GridpackWorkflow/production/ISRStau_DirectStau/jobs"
genprodir="/afs/cern.ch/work/d/dspitzba/SUSYsignalProduction/genproductions/"

PARTN1="_mN1-"

### Create cards and SLHAs for all mass points

#for MNLSP in 100 150 200 250 300 350 400; do
#for MNLSP in 100; do
for MNLSP in 400; do
  #for DM in 10 20 30 40 50; do
  for DM in 40; do
    if [ $MNLSP -eq 100 -a $DM -eq 10 ]
    then
      continue
    else
      MN1=`awk "BEGIN {printf \"%.2f\n\", (${MNLSP}-${DM})}"`
      MN1STR=${MN1/./p}
      MSTSTR=${MNLSP/./p}
      python ${SCRIPT} ${MODEL}${MSTSTR}${PARTN1}${MN1STR} --cards-dir ${JOBS}/${MODEL}${MSTSTR}${PARTN1}${MN1STR}  --genproductions-dir ${genprodir}
    fi
  done
done

