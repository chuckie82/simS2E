	#
	# What are the inputs?
	# Beamline description: prop_params.txt
	#
    echo "Welcome to prop"
    export $PYTHONPATH=$WORKDIR/packages/WPG:$PYTHONPATH
    cd $WORKDIR ;  pwd
    #JMAX=NUM_PROP_OUT;
    #myInd=$(printf %07d $JMAX)
    cd $WORKDIR/modules/prop
    python $WORKDIR/modules/prop/propagateSE.py --input-directory $ROOT/data/$PROJECT/FELsource --output-directory $ROOT/data/$PROJECT/prop --cpu-number 1
    #/afs/desy.de/group/exfel/software/karabo-trunk/extern/bin/python $ROOT/modules/prop/diagnostics.py --input-file $ROOT/data/$PROJECT/prop/prop_out_$myInd
