#!/bin/bash

echo "Starting SingFEL..."

# Directory where SingFEL is installed
SingFEL_DIR=$ROOT/packages/diffr/singfel
# Directory where simulation data will be stored
IO_DIR=$ROOT/data/$PROJECT
# Full path to the config file for this simulation
CONFIG=$ROOT/config/config_$PROJECT

echo "SingFEL_DIR: " $SingFEL_DIR
echo "IO_DIR: " $IO_DIR
echo "CONFIG: " $CONFIG

# Copy python script for preparing hdf5 structure
ln -s $ROOT/modules/diffr/prepHDF5.py /data/S2E/data/$PROJECT/prepHDF5.py

cd $SingFEL_DIR/build
make #&& 
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
#python2.7 $ROOT/modules/diffr/diagnostic_singfel.py $IO_DIR
