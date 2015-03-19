    # pmi (Z.J.)
    
    XMDYN=$ROOT/packages/XMDYN/exe/xmdyn_s2e.x
    NUM_PROP=100

    numID=`echo $ID|bc -w`
    (( PROP_ID = numID % NUM_PROP )) ; if [ $PROP_ID == 0 ] ; then PROP_ID=$NUM_PROP ; fi
    ID=$(printf %07d $numID)
    PROP_ID=$(printf %07d $PROP_ID)
    PROP_OUT_FILE=$PROJECT/prop/prop_out_$PROP_ID.h5
    PMI_OUT_FILE=$PROJECT/pmi/pmi_out_$ID.h5
    
    cd $ROOT ;  pwd
    mkdir -p $PROJECT/pmi

    #echo $PYTHON  ./modules/pmi/script.py  h5_out2in  $PROJECT/prop/prop_out_$PROP_ID.h5  $PROJECT/pmi/pmi_out_$ID.h5
    #$PYTHON  ./modules/pmi/script.py  h5_out2in  $PROJECT/prop/prop_out_$PROP_ID.h5  $PROJECT/pmi/pmi_out_$ID.h5
    echo $PYTHON  ./modules/pmi/script.py  h5_out2in  $PROP_OUT_FILE  $PMI_OUT_FILE
    $PYTHON  ./modules/pmi/script.py  h5_out2in  $PROP_OUT_FILE  $PMI_OUT_FILE

    echo $XMDYN   $PROJECT   $ID   $PROP_OUT_FILE
    echo $XMDYN   $PROJECT   $ID   $PROP_OUT_FILE
