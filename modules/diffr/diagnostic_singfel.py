#!/usr/bin/env python2.6
"""
prepHDF5.py:
Prepares hdf5 in S2E format
"""
import os
import sys
import h5py
import numpy as np
import matplotlib.pyplot as plt

def diagnose( projectDir ) :
    file_in  = h5py.File( projectDir + "/diffr/diffr_out_0000001.h5" , "r")
    diffr = file_in['data/diffr']
    plt.imshow(np.log(np.abs(diffr)),interpolation='none')
    plt.show()
    data = file_in['data/data']
    plt.imshow(data,interpolation='none')
    plt.show()    
    file_in.close()

# inputs to the script
if __name__ == '__main__':
    if len( sys.argv ) > 1 :
        projectDir  = sys.argv[1]
    diagnose( projectDir )
