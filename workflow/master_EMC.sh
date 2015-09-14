#!/bin/bash

echo "Starting EMC..."

#Compiles exectuables in the SRC directory; 
#needed for runEMC.py script.
cd ${SRC}
./compile_EMC

#Let's parse some options.
OPTS="-s ${SRC} -T ${TMP} -i ${INPUT} -o ${OUTPUT} -q ${INITIALQUAT} -Q ${MAXQUAT} -m ${MAXITER} -e ${MINERR} "
ADDOPT=" "
[$PLOT -eq 1] && {ADDOPT="${ADDOPT} -p"} 
[$DETAILED -eq 1] && {ADDOPT="${ADDOPT} -d"}
OPTS="${OPTS} ${ADDOPT}"

#Starts multiple reconstructions 
for i in `seq 1 ${NUMRECON}`;
do
    echo "Starting reconstruction ${i}."
    echo "Temporary output stored in ${TMP}."
    echo "Output stored in ${OUTPUT}."
	nohup python runEMC.py ${OPTS} &
	sleep ${SLEEPDUR}
done
