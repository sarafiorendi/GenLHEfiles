#!/bin/sh
JOBS="jobs"
TEMP="templatecards"
PROC="ISRStau_DirectStau"
PARTN1="_mN1-"
PARTST="_mStau-"

### Create cards and SLHAs for all mass points

for MNLSP in 100 150 200 250 300 350 400; do
  for DM in 10 20 30 40 50; do
    MN1=`awk "BEGIN {printf \"%.2f\n\", (${MNLSP}-${DM})}"` 
    MN1STR=${MN1/./p}
    MSTSTR=${MNLSP/./p}
    MODEL=${PROC}${PARTST}${MSTSTR}${PARTN1}${MN1STR}
    mkdir -p "${JOBS}/${MODEL}"
    cp ${TEMP}/${PROC}_run_card.dat "${JOBS}/${MODEL}/${MODEL}_run_card.dat"
    sed "s/%MNLSP%/${MSTSTR}/g;s/%MN1%/${MN1STR}/g" ${TEMP}/${PROC}_proc_card.dat > "${JOBS}/${MODEL}/${MODEL}_proc_card.dat"
    sed "s/%MN1%/${MN1}/g;s/%MNLSP%/${MNLSP}/g" ${TEMP}/${PROC}_customizecards.dat > "${JOBS}/${MODEL}/${MODEL}_customizecards.dat"
    sed "s/%MN1%/${MN1}/g;s/%MNLSP%/${MNLSP}/g" ${TEMP}/${PROC}.slha > ${JOBS}/${MODEL}/${MODEL}.slha
  done
done
