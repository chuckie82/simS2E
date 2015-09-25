#!/bin/bash

echo "Starting SingFEL..."

echo "SingFEL_DIR: " $SingFEL_DIR
echo "IO_DIR: " $IO_DIR
echo "CONFIG: " $CONFIG

# Copy python script for preparing hdf5 structure
cp $ROOT/modules/diffr/prepHDF5.py $ROOT/data/$PROJECT/prepHDF5.py

cd $SingFEL_DIR/build
make #&& 
mpirun -np $numProcesses $SingFEL_DIR/bin/radiationDamageMPI \
--inputDir $IO_DIR \
--outputDir $IO_DIR/diffr \
--configFile $CONFIG \
--beamFile $IO_DIR/diffr/s2e.beam \
--geomFile $IO_DIR/diffr/s2e.geom \
--uniformRotation $uniformRotation \
--calculateCompton $calculateCompton \
--sliceInterval $sliceInterval \
--numSlices $numSlices \
--pmiStartID $pmiStartID \
--pmiEndID $pmiEndID \
--numDP $numDP

# Copy the cpp file used in this project
cp $SingFEL_DIR/src/radiationDamageMPI.cpp $ROOT/data/$PROJECT/diffr/.

# Perform diagnostic
#python2.7 $ROOT/modules/diffr/diagnostic_singfel.py $IO_DIR
