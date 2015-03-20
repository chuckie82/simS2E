# Set permisisons
umask 002

ROOT=/data/S2E

# HELP
if [ -z "$1" ] ; then
    echo \
"Usage: $0 <PROJECT_DIR>  <MODULE> <ID>
   <MODULE>: FELsource , prop , pmi , diffr , orient , s2e 
   \`s2e\` stands for all modules of the pipeline
   S2E root dir: $ROOT
"
    exit
fi

# root directory of the simulation (project)
PROJECT=$1  ;  shift 1
MODULE=$1 ; shift 1
ID=$1 ; shift 1

if [ ! -z "$ID" ] ; then 
    ID=$(printf %07d $ID)
else
    ID=1
    ID=$(printf %07d $ID)
fi

PYTHON=/usr/bin/python2.7

########### Load input configuration ##########
. $ROOT/config/config_$PROJECT

########### FELsource ##########

if [ "x$MODULE" == xFELsource ] ||  [ "x$MODULE" == xs2e ]  ; then
    . master_${FELsource}.sh
fi

########### prop ##########

if [ "x$MODULE" == xprop ] ||  [ "x$MODULE" == xs2e ]  ; then
    . master_${PROP}.sh
fi

########### pmi ##########

if [ "x$MODULE" == xpmi ] ||  [ "x$MODULE" == xs2e ]  ; then
    . master_${PMI}.sh
fi

########### diffr ##########

if [ "x$MODULE" == xdiffr ] ||  [ "x$MODULE" == xs2e ]  ; then
    . master_${DIFFR}.sh
fi

########### orient ##########

if [ "x$MODULE" == xorient ] ||  [ "x$MODULE" == xs2e ]  ; then
    . master_${ORIENT}.sh
fi
