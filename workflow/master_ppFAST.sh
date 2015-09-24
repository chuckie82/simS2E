cd $WORKDIR ;  pwd

#
# number of skipped time slices
#
		
if [ "x$CHARGE" == x20pC ] ; then
    TRD1=1. ; 
    TRD2=7.
    NSKIP=7
fi
            
if [ "x$CHARGE" == x100pC ] ; then
    TRD1=3. ; 
	TRD2=29.
	NSKIP=12
fi    
            
if [ "x$CHARGE" == x250pC ] ; then
    TRD1=10. ; 
    TRD2=74.
    NSKIP=16    
fi

echo "Welcome to FELsource"
echo "CHARGE:"$CHARGE 
echo $(printf "%s : %s fs, NSKIP=%d" $TRD1 $TRD2 $NSKIP)
		
cd $WORKDIR/modules/FELsource ; pwd

JMAX=$NUM_FELsource_OUT;
 
for (( i=1; i<=$JMAX; i++ )); do
    myInd=$(printf %07d $i)
	myRunNum=$i
	if [ "x$CHARGE" == x100pC ]   ; then
		myRunNum=$(printf %04d $((i+1000)))
	fi
	echo $myInd
	echo $myRunNum
    python $WORKDIR/modules/FELsource/fast2h5_new_s2e_fake.py --output-dir=$ROOT/data/$PROJECT/FELsource 
done
#/afs/desy.de/group/exfel/software/karabo-trunk/extern/bin/python $ROOT/modules/FELsource/diagnostic_felsrc.py --input-file $ROOT/data/$PROJECT/FELsource/FELsource_out_$myInd

