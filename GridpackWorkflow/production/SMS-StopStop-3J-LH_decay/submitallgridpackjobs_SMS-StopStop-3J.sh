#!/bin/sh
SCRIPT="../../test/scripts/submitGridpackCondorJob_306000.py"
#MODEL="SMS-StopStop-3J_mStop-"
JOBS="jobs"

for MPROD in 225 275 ; do
    MLSP=50
    if [ $MPROD == "275" ]; then
	MLSP=100
    fi
    MODEL="SMS-StopStop-3J_mStop-"${MPROD}_mLSP-${MLSP}		
    #python ${SCRIPT} ${MODEL}${MPROD} --cards-dir ${JOBS}/${MODEL}${MPROD} --genproductions-dir ${genprodir} --proxy ${vomsdir}
    python ${SCRIPT} ${MODEL}  --cards-dir ${JOBS}/${MODEL} --proxy /tmp/x509up_u31701 --genproductions-dir /home/users/scodella/SUSYsignalProductionLO/genproductions/
done
