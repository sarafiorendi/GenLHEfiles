DUMMY='Need this to comment the following' 

DIRROOT='/eos/home-s/scodella/mcProduction/RAWSIM/'
MMIN=1000; MMAX=2800; MSTP=300
PROCESS="T1qqqq-LLChipm_ctau-10"; QMIN=125; QMAX=165; QSTP=5

#DIRROOT='/eos/cms/store/user/scodella/mcProduction/RAWSIM/'
#MMIN=300; MMAX=2600; MSTP=300
#PROCESS="T2qq-LLChipm_ctau-10"; QMIN=60; QMAX=80; QSTP=2

#DIRROOT='/eos/cms/store/caf/user/scodella/mcProduction/RAWSIM/'
#MMIN=400; MMAX=1500; MSTP=300
#PROCESS="T2bt-LLChipm_ctau-10"; QMIN=60; QMAX=80; QSTP=2

MODEL="SMS-${PROCESS}_mSq-"

for MGL in `eval echo {$MMIN..$MMAX..$MSTP}`; do
    for QCUT in `eval echo {$QMIN..$QMAX..$QSTP}`; do
	FILES=$DIRROOT$MODEL$MGL"/GEN_"$MODEL$MGL"_*_"$QCUT.root
	OUTTEXT=$MODEL$MGL"_"$QCUT
	echo $FILES
	root -l -b -q '../../../test/scripts/plotdjr.C('\"$FILES\"', '\"$OUTTEXT\"')'
    done
    mkdir -p Plots/$MODEL$MGL
    cp Plots/index.php Plots/$MODEL$MGL/
    mv $MODEL$MGL*.pdf Plots/$MODEL$MGL/
    mv $MODEL$MGL*.txt Plots/$MODEL$MGL/
done
