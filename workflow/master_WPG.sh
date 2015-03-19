	#
	# What are the inputs?
	# Beamline description: prop_params.txt
	#
    echo "Welcome to prop"
    cd $ROOT ;  pwd
    JMAX=NUM_PROP_OUT;
    myInd=$(printf %07d $JMAX)
    cd $ROOT/modules/prop
    /afs/desy.de/group/exfel/software/karabo-trunk/extern/bin/python $ROOT/modules/prop/propagateSE.py --input-directory $ROOT/data/$PROJECT/FELsource --output-directory $ROOT/data/$PROJECT/prop --cpu-number 8
    /afs/desy.de/group/exfel/software/karabo-trunk/extern/bin/python $ROOT/modules/prop/diagnostics.py --input-file $ROOT/data/$PROJECT/prop/prop_out_$myInd
