#!/bin/bash

if [ ! -z "`hostname|grep cfel-t-`" ] ; then
    PYTHON=python2.6
fi


########### pmi ##########

if [ "x$MODULE" == xpmi ] ||  [ "x$MODULE" == xs2e ]  ; then
    # pmi (Z.J.)
    
    #PMI_EXE=$ROOT/packages/XMDYN/exe/xmdyn_s2e.x
    PMI_EXE="$PYTHON $ROOT/packages/pmi_demo/pmi_demo.py"
    #NUM_PROP=100
    #NUM_PROP=`ls $PROJECT/prop/prop_out_???????.h5|nl|tail -n1|awk -F\  '{print $1}'`
    echo "Number of prop_out files:  $NUM_PROP_OUT" >&2
    PMI_OPT_CREATE_PMI_OUT=1   ;   PMI_OPT_RUN_PMI=1   ;   PMI_EXE_ARGS=

    #ARGS="`echo $*`"
    #while [ ! -z "$ARGS" ] ; do
    #    VAL=${ARGS%%\ *}  ;  ARGS="${ARGS#*\ }"
    #    if [  "$ARGS" == "${ARGS#*\ }" ] ; then ARGS= ; fi
    #done

##################################################
################  TESTING STARTS  ################
#                                                #
  if [ `basename $0` == master_pmi.sh ] ; then
    ROOT=`pwd`
    PMI_EXE=$ROOT/packages/XMDYN/exe/xmdyn_s2e.x
    export LD_LIBRARY_PATH=$ROOT/src/extra/hdf5/lib:$LD_LIBRARY_PATH
    echo $LD_LIBRARY_PATH
    PMI_OPT_CREATE_PMI_OUT=0   ;   PMI_OPT_RUN_PMI=0
    PMI_JUMP_OUT=0
    while [ ! -z "$1" ] && [ $PMI_JUMP_OUT == 0 ] ; do
        case "$1" in
            -pmi_out )   PMI_OPT_CREATE_PMI_OUT=1  ;  shift 1 ;;
            -pmi_run )   PMI_OPT_RUN_PMI=1  ;         shift 1 ;;
            -exe )       PMI_EXE=$2  ;          shift 2 ;;
            *) PMI_JUMP_OUT=1 ;;
        esac
    done
    PMI_EXE_ARGS="$@"
  fi
#                                                #
###############   TESTING ENDS   #################
##################################################
    

    PMI_numID=`echo $ID|bc -w`
    (( PMI_PROP_ID = PMI_numID % NUM_PROP_OUT )) ; if [ $PMI_PROP_ID == 0 ] ; then PMI_PROP_ID=$NUM_PROP_OUT ; fi
    PMI_ID=$(printf %07d $PMI_numID)
    PMI_PROP_ID=$(printf %07d $PMI_PROP_ID)
    PMI_PROP_OUT_FILE=$ROOT/data/$PROJECT/prop/prop_out_$PMI_PROP_ID.h5
    PMI_OUT_FILE=$ROOT/data/$PROJECT/pmi/pmi_out_$ID.h5
    
    #cd $ROOT ;  pwd
    mkdir -p $PROJECT/pmi

    #echo $PYTHON  ./modules/pmi/script.py  h5_out2in  $PROJECT/prop/prop_out_$PROP_ID.h5  $PROJECT/pmi/pmi_out_$ID.h5
    #$PYTHON  ./modules/pmi/script.py  h5_out2in  $PROJECT/prop/prop_out_$PROP_ID.h5  $PROJECT/pmi/pmi_out_$ID.h5
    echo $PYTHON  ./modules/pmi/script.py  h5_out2in  $PMI_PROP_OUT_FILE  $PMI_OUT_FILE
    if [ 1 == $PMI_OPT_CREATE_PMI_OUT ] ; then 
        $PYTHON  $ROOT/modules/pmi/script.py  h5_out2in  $PMI_PROP_OUT_FILE  $PMI_OUT_FILE  
    fi

    PMI_PWD=`pwd` ; cd $ROOT
    echo $PMI_EXE   $PROJECT   $ID   $PMI_PROP_OUT_FILE $PMI_EXE_ARGS
    if [ 1 == $PMI_OPT_RUN_PMI ] ; then 
        $PMI_EXE   $PROJECT   $ID   $PMI_PROP_OUT_FILE  $PMI_EXE_ARGS ; 
    fi
    cd "$PMI_PWD"

fi

