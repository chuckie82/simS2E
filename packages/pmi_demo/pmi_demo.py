#!/usr/bin/python2.6

import sys
import os
import commands

import datetime
import time

import string
import copy

#import shelve
#import cPickle

import h5py

import select
import numpy
import scipy.interpolate

import scipy

import matplotlib
matplotlib.use('Agg')
import pylab

import random


##############################################################################

global g_s2e 
global g_dbase


##############################################################################

def f_s2e_setup() :
    global g_s2e 
    g_s2e = dict() ;
    g_s2e['setup'] = dict()
    g_s2e['sys'] = dict()
    g_s2e['setup']['num_digits'] = 7
    g_s2e['steps'] = 100 
    g_s2e['maxZ'] = 26


##############################################################################

def f_save_info() :
    g_s2e['setup']['pmi_out'] = 'data/' + g_s2e['prj'] + '/pmi/pmi_out_' + str( g_s2e['id'] ).zfill(g_s2e['setup']['num_digits'])  + '.h5'
    pmi_file = g_s2e['setup']['pmi_out']

    grp = '/info'
###    print pmi_file , grp
    xfp  = h5py.File( pmi_file , "a" )
    try:
        grp_hist_parent = xfp.create_group( grp ) 
    except:
        1

#    xfp[ grp + '/Sq_free' ] = g_dbase['Sq_free']
    xfp.close()





##############################################################################

def f_init_random() :
    random.seed( g_s2e['id'] )


##############################################################################

def f_dbase_Zq2id( a_Z , a_q ) :
    return ( a_Z * ( a_Z + 1 ) ) / 2 - 1*1 + a_q

##############################################################################


def f_dbase_setup() :
    global g_dbase
    print '   Update database!!!'
    g_dbase = dict()
    g_dbase['halfQ'] = numpy.array( [ 0 , 1 , 2 ] ) ; 
    maxZ = g_s2e['maxZ']  #99 
    g_dbase['ff'] = numpy.zeros( ( f_dbase_Zq2id( maxZ , maxZ ) + 1 , len( g_dbase['halfQ'] ) ) )
    ii = 0 
    for ZZ in range( 1 , maxZ+1 ) :
        for qq in range( ZZ+1 ) :
            g_dbase['ff'][ ii , : ] = numpy.array( [ 1.0 , 0.5 , 0.25 ] ) * ( ZZ - qq ) ; 
###            print ZZ,  qq, ii
###            print  g_dbase['ff'][ ii , : ]
            ii = ii + 1
    g_dbase['Sq_halfQ'] = numpy.array( [ 0 , 0 , 0 ] ) ; 
    g_dbase['Sq_bound'] = numpy.array( [ 0 , 0 , 0 ] ) ; 
    g_dbase['Sq_free']  = numpy.array( [ 0 , 0 , 0 ] ) ; 
#    g_dbase['ph_sigma'] ;



##############################################################################


def f_hdf5_simple_read( a_file , a_dataset ) :
    xfp  = h5py.File( a_file , "r" )
    xxx = xfp.get( a_dataset ).value
    xfp.close()
    return xxx


##############################################################################


def f_load_snp_content( a_fp , a_snp ) :
    global g_s2e
    dbase_root = "/data/snp_" + str( a_snp ).zfill(g_s2e['setup']['num_digits']) + "/" 
    xsnp = dict() 
    xsnp['Z']   = a_fp.get( dbase_root + 'Z' )   .value
    xsnp['T']   = a_fp.get( dbase_root + 'T' )   .value
    xsnp['ff']  = a_fp.get( dbase_root + 'ff' )  .value
    xsnp['xyz'] = a_fp.get( dbase_root + 'xyz' ) .value
    xsnp['r']   = a_fp.get( dbase_root + 'r' )   .value
    N = xsnp['Z'].size 
    xsnp['q'] = numpy.array( [ xsnp['ff'][ pylab.find( xsnp['T'] == x ) , 0 ]  for x in xsnp['xyz'] ] ) .reshape(N,)
    xsnp['snp'] = a_snp ;

    return xsnp


##############################################################################


def f_load_snp_xxx( a_real , a_snp ) :
    global g_s2e
    xfp  = h5py.File( g_s2e['prj'] + '/pmi/pmi_out_' + str( a_real ).zfill(g_s2e['setup']['num_digits'])  + '.h5' , "r" )
    xsnp = f_load_snp_content( xfp , a_snp )
    xfp.close()
    return xsnp


##############################################################################


def f_load_sample( ) :
    global g_s2e
    sample = dict()
    xfp = h5py.File( 'data/' + g_s2e['prj'] + '/sample/sample.h5' , "r" )
    xxx = xfp.get( 'Z' )   ;  sample['Z']   = xxx.value
    xxx = xfp.get( 'r' )   ;  sample['r']   = xxx.value
    xfp.close()
    sample['selZ'] = dict()
    for sel_Z in numpy.unique( sample['Z'] ) :
        sample['selZ'][sel_Z] = pylab.find( sel_Z == sample['Z'] )
    sample['N'] = len( sample['Z'] ) 

    g_s2e['sample'] = sample


##############################################################################

def f_save_data( dset , data ) :
    xfp  = h5py.File( g_s2e['setup']['pmi_out'] , "a" )
    try:
        xfp.create_group( os.path.dirname( dset ) )
    except:
        1

    xfp[ dset ] = data
    xfp.close()



##############################################################################


def f_rotate_sample() :
    print '   quaternion to be set!!!'
    g_s2e['sample']['rot_quaternion'] = numpy.random.rand( 4 ) #  pylab.array([0,0,0,0])
    g_s2e['sample']['rotmat'] = pylab.zeros((9,))
    s2e_gen_randrot_quat( g_s2e['sample']['rot_quaternion'] ,  g_s2e['sample']['rotmat'] ) ;
    s2e_rand_orient( g_s2e['sample']['r'] , g_s2e['sample']['rotmat'] ) ;

    f_save_data( '/data/angle' , g_s2e['sample']['rot_quaternion'] )




##############################################################################





def s2e_gen_randrot_quat( quat , rotmat ) :

        if ( 0 == quat[0] * quat[0] + 
                  quat[1] * quat[1] +
                  quat[2] * quat[2] +
                  quat[3] * quat[3] ) :
            u0 = pylab.rand( 1 ) ; u1 = pylab.rand( 1 ) ; u2 = pylab.rand( 1 ) ; 
            q0 = pylab.sqrt(1-u0) * pylab.sin(2*pylab.pi*u1) ;
            q1 = pylab.sqrt(1-u0) * pylab.cos(2*pylab.pi*u1) ;
            q2 = pylab.sqrt(u0) * pylab.sin(2*pylab.pi*u2) ;
            q3 = pylab.sqrt(u0) * pylab.cos(2*pylab.pi*u2) ;

            quat[0] = q0 ;
            quat[1] = q1 ;
            quat[2] = q2 ;
            quat[3] = q3 ;

        else :
            q0 = quat[0] ;
            q1 = quat[1] ;
            q2 = quat[2] ;
            q3 = quat[3] ;

        rotmat[0] = q0*q0 + q1*q1 - q2*q2 - q3*q3 ;  #// M[0][0]
        rotmat[1] = 2 * ( q1*q2 - q0*q3 ) ;          #// M[0][1]
        rotmat[2] = 2 * ( q1*q3 + q0*q2 ) ;          #// M[0][2]
        rotmat[3] = 2 * ( q1*q2 + q0*q3 ) ;          #// M[1][0]
        rotmat[4] = q0*q0 - q1*q1 + q2*q2 - q3*q3 ;  #// M[1][1]
        rotmat[5] = 2 * ( q2*q3 - q0*q1 ) ;          #// M[1][2]
        rotmat[6] = 2 * ( q1*q3 - q0*q2 ) ;          #// M[2][0]
        rotmat[7] = 2 * ( q2*q3 + q0*q1 ) ;          #// M[2][1]
        rotmat[8] = q0*q0 - q1*q1 - q2*q2 + q3*q3 ;  #// M[2][2]



#        inversematrix3( (void*) (rotmat + ii) , (void*) (invmat + ii) ) ;

#    for ( ii = 0 ; ii < randrot ; ii++ )
#    {
#        for ( jj=0 ; jj < 3 ; jj++ )
#        {
#            printf( "% e % e % e\n" , rotmat[ii][jj*3+0] ,  rotmat[ii][jj*3+1] , 
#                                      rotmat[ii][jj*3+2] ) ;
#        }
#        printf("\n") ;

#        for ( jj=0 ; jj < 3 ; jj++ )
#        {
#            printf( "% e % e % e\n" , invmat[ii][jj*3+0] ,  invmat[ii][jj*3+1] , 
#                                      invmat[ii][jj*3+2] ) ;
#        }
#        printf("\n\n\n") ;
#    }
#}



##############################################################################



def s2e_rand_orient( r ,mat ) :
    N = r.shape[1]
###    print N
    vv = pylab.zeros((3,0)) ;

    for ii in range(N) :
        vv = r[ii,:]
###        print vv , vv.shape , mat.shape
        r[ii,0] = mat[0] * vv[0] + mat[1] * vv[1] + mat[2] * vv[2] ;
        r[ii,1] = mat[3] * vv[0] + mat[4] * vv[1] + mat[5] * vv[2] ;
        r[ii,2] = mat[6] * vv[0] + mat[7] * vv[1] + mat[8] * vv[2] ;




##############################################################################

def f_system_setup() :
    global g_s2e

    g_s2e['sys']['r'] = g_s2e['sample']['r'].copy() 
    g_s2e['sys']['q'] = pylab.zeros( g_s2e['sample']['Z'].shape )
    g_s2e['sys']['NE'] = g_s2e['sample']['Z'].copy()
    g_s2e['sys']['Z'] = g_s2e['sample']['Z']
    g_s2e['sys']['Nph'] = 1e99
    print '   Update Nph!!!'


##############################################################################

def f_save_snp( a_snp ) :
    global g_s2e 

    g_s2e['sys']['xyz'] = f_dbase_Zq2id( g_s2e['sys']['Z'] , g_s2e['sys']['q'] )
    g_s2e['sys']['T'] = pylab.sort( pylab.unique( g_s2e['sys']['xyz'] ) )
    ff = numpy.zeros( ( len( g_s2e['sys']['T'] ) , len( g_dbase['halfQ'] ) ) )
    for ii in range( len( g_s2e['sys']['T'] ) ) :
        ff[ii,:] =  g_dbase['ff'][g_s2e['sys']['T'][ii].astype(int),:].copy()
###        print g_s2e['sys']['T'][ii].astype(int) , ff[ii,:] 

    pmi_file = g_s2e['setup']['pmi_out']
    grp = '/data/snp_' + str( a_snp ).zfill( g_s2e['setup']['num_digits'] )
###    print pmi_file , grp
    xfp  = h5py.File( pmi_file , "a" )
    try:
        grp_hist_parent = xfp.create_group( '/data' ) 
    except:
        1
    grp_hist_parent = xfp.create_group( grp ) 
    xfp[ grp + '/Z' ]   = g_s2e['sys']['Z']
    xfp[ grp + '/T' ]   = g_s2e['sys']['T']
    xfp[ grp + '/xyz' ] = g_s2e['sys']['xyz']
    xfp[ grp + '/r' ] = g_s2e['sys']['r']
    xfp[ grp + '/Nph' ] = g_s2e['sys']['Nph']
    xfp[ grp + '/halfQ' ] = g_dbase['halfQ']
    xfp[ grp + '/ff' ] = ff
    xfp[ grp + '/Sq_halfQ' ] = g_dbase['Sq_halfQ']
    xfp[ grp + '/Sq_bound' ] = g_dbase['Sq_bound']
    xfp[ grp + '/Sq_free' ] = g_dbase['Sq_free']

    xfp.close()




##############################################################################


def f_num_snp_xxx( all_real ) :
    global g_s2e 
    xfp  = h5py.File( g_s2e['prj'] + '/pmi/pmi_out_' + str( all_real[0] ).zfill(g_s2e['setup']['num_digits'])  + '.h5' , "r" )
    cc = 1 
    while 1 :
        if not  xfp.get( "/data/snp_" + str( cc ).zfill(g_s2e['setup']['num_digits']) )  :
            xfp.close()
            return cc - 1 
        cc = cc + 1

#        try: 
#            if type( a_fp.get( "/data/snp_" + str( cc ).zfill(NUM_DIGITS) + '/Nph' ) ) == 'NoneType' :
#                print 'N'
#            else :
#                print 1
#       
#        except:
#            return cc


##############################################################################

def f_load_pulse( a_prop_out ) :
    global g_s2e

    xfp  = h5py.File( a_prop_out , "r" )
    g_s2e['pulse'] = dict() 
    g_s2e['pulse']['xFWHM']   = xfp.get( '/misc/xFWHM' )   .value
    g_s2e['pulse']['yFWHM']   = xfp.get( '/misc/yFWHM' )   .value
    g_s2e['pulse']['nSlices']   = xfp.get( 'params/Mesh/nSlices' )   .value
    g_s2e['pulse']['nx']   = xfp.get( 'params/Mesh/nx' )   .value
    g_s2e['pulse']['ny']   = xfp.get( 'params/Mesh/ny' )   .value
    g_s2e['pulse']['sliceMax']   = xfp.get( 'params/Mesh/sliceMax' )   .value
    g_s2e['pulse']['sliceMin']   = xfp.get( 'params/Mesh/sliceMin' )   .value
    g_s2e['pulse']['xMax']   = xfp.get( 'params/Mesh/xMax' )   .value
    g_s2e['pulse']['xMin']   = xfp.get( 'params/Mesh/xMin' )   .value
    g_s2e['pulse']['yMax']   = xfp.get( 'params/Mesh/yMax' )   .value
    g_s2e['pulse']['yMin']   = xfp.get( 'params/Mesh/yMin' )   .value
    g_s2e['pulse']['photonEnergy']   = xfp.get( 'params/photonEnergy' )   .value
    g_s2e['pulse']['arrEver']   = xfp.get( 'data/arrEver' )   .value
    g_s2e['pulse']['arrEhor']   = xfp.get( 'data/arrEhor' )   .value
    #g_s2e['pulse']['']   = xfp.get( '' )   .value
    xfp.close()

#    g_s2e_pulse['sliceMax']   = g_s2e_pulse[''] - g_s2e_pulse[''] 
#    g_s2e_pulse['sliceMin']   = 0
#    g_s2e_pulse['sliceDelta']   = g_s2e_pulse['']  / ( g_s2e_pulse[''] - 1.0 )

#    g_s2e_pulse['slices']   =

#    g_s2e_pulse['xMax']   = ( g_s2e_pulse[''] - g_s2e_pulse[''] ) / 2.0
#    g_s2e_pulse['xMin']   = - g_s2e_pulse['']
#    g_s2e_pulse['xDelta']   = ( g_s2e_pulse[''] - g_s2e_pulse[''] ) / ( g_s2e_pulse[''] - 1.0 )

#    g_s2e_pulse['sel_pix_x']   = ( g_s2e_pulse[''] + 1 ) / 2
#    g_s2e_pulse['sel_pix_y']   = ( g_s2e_pulse[''] + 1 ) / 2

    return


#    /**  Some transformation  and  derived useful parameters  */ 
#    data_prop_out.sliceMax = data_prop_out.sliceMax - data_prop_out.sliceMin ;
#    data_prop_out.sliceMin = 0 ;
#
#    data_prop_out.sliceDelta = data_prop_out.sliceMax / (double) (data_prop_out.nSlices-1) ;

#    data_prop_out.slices = calloc( data_prop_out.nSlices , sizeof(double) ) ;
#    for ( ii = 0 ; ii < data_prop_out.nSlices ; ii++ )
#    {
#        data_prop_out.slices[ii] = data_prop_out.sliceDelta * ii ;
#    }

#    data_prop_out.xMax =  ( data_prop_out.xMax - data_prop_out.xMin ) / 2.0 ;
#    data_prop_out.xMin = - data_prop_out.xMax ;
#    data_prop_out.xDelta = ( data_prop_out.xMax - data_prop_out.xMin ) / 
#                           (double) (data_prop_out.nx - 1 ) ;

#    data_prop_out.yMax =  ( data_prop_out.yMax - data_prop_out.yMin ) / 2.0 ;
#
#    data_prop_out.yMin = - data_prop_out.yMax ;
#    data_prop_out.yDelta = ( data_prop_out.yMax - data_prop_out.yMin ) / 
#                           (double) ( data_prop_out.ny - 1 ) ;

#    /**  Selecting center (ot highest fluence) pixel */
#    data_prop_out.sel_pix_x = ( data_prop_out.nx + 1 ) / 2 ;
#    data_prop_out.sel_pix_y = ( data_prop_out.ny + 1 ) / 2 ;



##############################################################################


def f_eval_disp( a_snp , a_r0 , a_sample ) :

    num_Z = len( a_sample['selZ'].keys() )
    all_disp = numpy.zeros( ( num_Z , ) )
    cc = 0 ;
    for sel_Z in a_sample['selZ'].keys() :
        dr = a_snp['r'][a_sample['selZ'][sel_Z],:] - a_r0[a_sample['selZ'][sel_Z],:]
        all_disp[cc] = numpy.mean( numpy.sqrt( numpy.sum( dr * dr , axis = 1 ) ) ) / 1e-10
        cc = cc + 1 
    return all_disp 


##############################################################################


def f_eval_numE( a_snp , a_sample ) :

    num_Z = len( a_sample['selZ'].keys() )
    all_numE = numpy.zeros( ( num_Z , ) )
    cc = 0 ;
    for sel_Z in a_sample['selZ'].keys() :
        all_numE[cc] = numpy.mean( a_snp['q'][a_sample['selZ'][sel_Z]] )
        cc = cc + 1 
    return all_numE 


##############################################################################


def f_md_step( r , v , m , dt ) :
    r = r.copy()
    v = v.copy()
    a = ( force( config , param ) + external_force( config , param ) ) / m
    r = r + v*dt + 0.5*a*dt**2.0 
    config['r'] = r
    an = ( force( config , param ) + external_force( config , param ) ) / m
    v = v + 0.5* (a+an) * dt
    config['v'] = v
    E = f_sysenergy_kin(v,m) + syspot( config , param ) + ext_syspot( config , param )


##############################################################################

def f_time_evolution() :

    for step in range( 1 , g_s2e['steps'] + 1 ) :
        f_save_snp( step )

##############################################################################


def   f_pmi_diagnostics_help() :
    print """
    ----
    """


##############################################################################
##############################################################################
##############################################################################




##############################################################################



### if to be called from command line:
if __name__ == '__main__':


    basename = sys.argv[0] .rstrip() .split('/')[-1]
    #basename = a_field .split('/')[-1]
    #dirname = a_field[ 0 : len(a_field) - len(basename) ] .strip('/') .rstrip('/')

#    if basename != 'pmi_placeholder.py' :

#        if len( sys.argv ) > 1 :
#            pmi_diagnostics( sys.argv[1:] )

#        else:
#            f_pmi_diagnostics_help()
#            print sys.argv[0] , basename


#    else :

    if len( sys.argv ) > 3 :
        print '===PMI_DEMO ... Go!'

        f_s2e_setup()
        f_dbase_setup()

        g_s2e['prj'] = sys.argv[1] ;
        g_s2e['id'] = sys.argv[2] ;
        g_s2e['prop_out'] = sys.argv[3] ;

        f_init_random()

        f_save_info()

#            f_load_pulse( g_s2e['prop_out'] )
#            print g_s2e['pulse']['xFWHM'] 

        f_load_sample()
        f_rotate_sample()

        f_system_setup()

        f_time_evolution()

        print '===PMI_DEMO ... Finished!'

    else:
        print 'help'
        #f_pmi_placeholder_help()


