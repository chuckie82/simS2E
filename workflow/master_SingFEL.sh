#!/bin/bash

echo "Starting SingFEL..."

SingFEL_DIR="/slicetest/yoon/singfel"
IO_DIR=$SingFEL_DIR/dataS2E/$PROJECT
CONFIG=$ROOT/workflow/config_$PROJECT

echo "SingFEL_DIR: " $SingFEL_DIR
echo "IO_DIR: " $IO_DIR
echo "CONFIG: " $CONFIG

cd $SingFEL_DIR/build
make &&
mpirun -np $numProcesses -f $hostFile $SingFEL_DIR/bin/radiationDamageMPI \
--input_dir = $IO_DIR \
--output_dir = $IO_DIR/diffr \
--config_file = $CONFIG \
-b $IO_DIR/diffr/s2e.beam \
-g $IO_DIR/diffr/s2e.geom \
--uniformRotation = $uniformRotation \
--calculateCompton = $calculateCompton \
--sliceInterval = $sliceInterval \
--numSlices = $numSlices \
--pmiStartID = $pmiStartID \
--pmiEndID = $pmiEndID \
--numDP = $numDP

# Copy the cpp file used in this project
cp $SingFEL_DIR/src/radiationDamageMPI.cpp $ROOT/data/$PROJECT/diffr/.

# Perform diagnostic
python $ROOT/modules/diffr/diagnostic_singfel.py $IO_DIR
