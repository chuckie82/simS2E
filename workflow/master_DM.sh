#!/bin/bash

echo "Starting DM..."

#Compiles exectuables in the SRC directory; 
#needed for runDM.py script.
echo $SRC_DM
cd ${SRC_DM}
./compile_DM
   
#Starts multiple reconstructions 
for i in `seq 1 ${NUMRECON_DM}`;
do
    echo "Starting reconstruction ${i}."
    #nohup 
    python runDM.py -s ${SRC_DM} -T ${TMP_DM} -i ${INPUT_DM} -o ${OUTPUT_DM} -r ${NUMTRIALS_DM} -a ${STARTAVE_DM} -n ${NUMITER_DM} -l ${LEASH_DM} -c ${SHRINKCYCLES_DM} &
	sleep ${SLEEPDUR_DM}
done
