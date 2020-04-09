#!/bin/sh
JOBS="jobs"
TEMP="templatecards"
PROC="SMS-StopStop-3J"
PART="_mStop-"

### Create cards and SLHAs for all mass points

for MPROD in 225 275 ; do
    MLSP=50
    if [ $MPROD == "275" ]; then
	MLSP=100
    fi			 	
    MODEL=${PROC}${PART}${MPROD}_mLSP-${MLSP}
    mkdir -p "${JOBS}/${MODEL}"
    cp ${TEMP}/${PROC}_run_card.dat "${JOBS}/${MODEL}/${MODEL}_run_card.dat"
    sed "s/%MPROD%/${MPROD}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}_proc_card.dat > "${JOBS}/${MODEL}/${MODEL}_proc_card.dat"
    sed "s/%MPROD%/${MPROD}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}_customizecards.dat > "${JOBS}/${MODEL}/${MODEL}_customizecards.dat"
    sed "s/%MPROD%/${MPROD}/g;s/%MLSP%/${MLSP}/g" ${TEMP}/${PROC}.slha > ${JOBS}/${MODEL}/${MODEL}.slha
done
