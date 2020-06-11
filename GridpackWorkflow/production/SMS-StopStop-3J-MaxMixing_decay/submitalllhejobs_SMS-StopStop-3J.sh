#!/bin/sh
SCRIPT="../../test/scripts/submitLHECondorJob.py"
MODEL="SMS-StopStop-3J_mStop-"

#for MPROD in 185; do
for MPROD in 155; do
    #echo /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}${MPROD}/${MODEL}${MPROD}_tarball.tar.xz 
    python ${SCRIPT} ${MODEL}${MPROD} --in-file /hadoop/cms/store/user/${USER}/mcProduction/GRIDPACKS/${MODEL}${MPROD}/${MODEL}${MPROD}_tarball.tar.xz  --proxy /tmp/x509up_u31701 --nevents 5000 --njobs 1
done


