#!/bin/bash
JOBS="jobs"
TEMP="templatecards"
PROC="SMS-TStauStau-MM"

### Create cards and SLHAs for all mass points

for MNLSP in {50..600..25} ;do
    MODEL=${PROC}"_mStau-"${MNLSP}
    mkdir -p "${JOBS}/${MODEL}"
    cp ${TEMP}/${PROC}_run_card.dat "${JOBS}/${MODEL}/${MODEL}_run_card.dat"
    sed "s/%MNLSP%/${MNLSP}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}_proc_card.dat > "${JOBS}/${MODEL}/${MODEL}_proc_card.dat"
    sed "s/%MNLSP%/${MNLSP}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}_customizecards.dat > "${JOBS}/${MODEL}/${MODEL}_customizecards.dat"
    sed "s/%MNLSP%/${MNLSP}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}.slha > ${JOBS}/${MODEL}/${MODEL}.slha
    
done

