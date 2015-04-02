import os
import sys
import h5py
import numpy as np
import multiprocessing as mp

def f_h5_out2in( src , dest , *args ) :

    file_in  = h5py.File( src , "r")
    file_out =  h5py.File( dest , "w")

    grp_hist = file_out.create_group( "history" )
    grp_hist_parent = file_out.create_group( "history/parent" )
    grp_hist_parent_detail = file_out.create_group( "history/parent/detail" )

    pre_s2e_module = os.path.basename( os.path.dirname( os.path.abspath( src ) ) )
    print 'Previous module: ' , pre_s2e_module
    
    # Add attribute to history/parent
    grp_hist_parent.attrs['name'] =  "_" + pre_s2e_module
    
    grp_srchist = file_in.get( "history/parent" ) ;
    file_out.copy( grp_srchist , grp_hist_parent )

    # Copy everything to history except "data" & "history"  
    for objname in file_in.keys() :
        if   objname != "data" \
             and   objname != "history" :
            x = file_in.get( objname )
            if file_in.get( objname , getclass = True )  == h5py.highlevel.Dataset :
                mygroup = file_in['/']
                file_out["history/parent/detail/"+objname] = mygroup[objname][...]
            elif file_in.get( objname , getclass = True )  == h5py.highlevel.Group :
                file_out.copy( x , "history/parent/detail/" + objname )
            else:
                print objname  , " has been SKIPPED!!"
                #file_out.copy( x , os.path.dirname( "history/parent/detail/" + objname ) )
                #file_in.get( objname ) .copy( os.path.dirname( "history/parent/detail/" + objname ) )
            #file_out.copy( x , "history/parent/detail/" )
            print objname 
        else :
            print '  NOT:', objname

    print file_in['data'].keys()
    print file_in['data'].items()    

    # Create external link to parent's data
    #file_out['history/parent/detail/data'] = h5py.ExternalLink( src ,'/data')
    parent_module = os.path.basename( src ) [ : os.path.basename( src ) .find( '_out' ) ] 
    file_out['history/parent/detail/data'] = h5py.ExternalLink( '../' + parent_module + '/' + os.path.basename( src ) , '/data' )
    

    # Create your own groups
    grp_data = file_out.create_group( "data" )
    grp_param = file_out.create_group( "params" )
    grp_param = file_out.create_group( "misc" )
    grp_param = file_out.create_group( "info" )

	# Create s2e interface version  
    interface = file_out.create_dataset("info/interface_version", (1,), dtype='f')
    interface[0] = 1.0

    file_out.close()
    file_in.close()

# inputs to the script
if __name__ == '__main__':
    if len( sys.argv ) > 1 :

        xcommand = sys.argv[1]

        if xcommand == 'h5_out2in' :
            src  = sys.argv[2]
            dest = sys.argv[3]
            f_h5_out2in( src , dest ) 
