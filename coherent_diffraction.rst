.. _coherent_diffraction:

.. image:: _static/detector.png
    :scale: 33 %

====================
Coherent Diffraction
====================

Input/Output data description
-----------------------------

The input/output data is expected in hdf5 format, and the glossary can be found below. Coherent diffraction module is responsible for reading in and writing out in the format specified below.

diffr_params_SingFEL (Input Parameter glossary)
-----------------------------------------------

===============  ==========================================================  ==========
Field name       Description                                                 DataType
===============  ==========================================================  ==========
--input_dir      Input directory where pmi_out files are stored              String
--output_dir     Output directory where diffr_out files will be stored       String
--config_file    Full path and filename of this file                         String 	 
-b               Experimental beam file                                      String 	 
-g               Experimental geometry file                                  String 	 
--sliceInterval  Interval to calculates diffraction                          Int 	 
--numSlices      Number of time slices to use for calculating diffraction    Int 	 
--pmiStartID     Start ID of PMI trajectory                                  Int 	 
--pmiEndID       End ID of PMI trajectory                                    Int 	 
--dpID           Diffraction pattern index for current pmiID                 Int 	 
--numDP          Number of diffraction patterns to generate per pmiID        Int 	 
--USE_GPU        Options to use GPU (1) or not (0)                           Int  	 
version          SingFEL version                                             0.1
===============  ==========================================================  ==========

diffr_out_XXXXXXX.h5 (Output HDF glossary)
------------------------------------------

+--------------------------+---------------------------------------------------------------------+-----------+----------+
| Field name               | Description                                                         | Data type | Units    |
+==========================+=====================================================================+===========+==========+
| data/                    |                                                                     |           |          |
+--------------------------+---------------------------------------------------------------------+-----------+----------+
| data/data                | Diffraction pattern in 2D matrix |                                  | Float     |          |
+--------------------------+---------------------------------------------------------------------+-----------+----------+
| data/diffr               | Diffracted intensity before Poisson noise (Optional)                | Float     |          |
+--------------------------+---------------------------------------------------------------------+-----------+----------+
| data/angle               | Additional rotation applied to the rotated pmi_out position.        |           |          |
|                          | Initial rotation angle can be found in pmi_out/data/angle.          | Float     |          |
|                          | Active right handed rotations applied in quaternion.                |           |          |
+--------------------------+---------------------------------------------------------------------+-----------+----------+
| history/                 | Information about input data                                        |           |          |
+--------------------------+---------------------------------------------------------------------+-----------+----------+
| history/parent/detail    | Details of the parent including /data, /info, /misc, /params        |           |          |
|                          | /data should be soft-linked with a relative path                    |           |          |
+--------------------------+---------------------------------------------------------------------+-----------+----------+
| history/parent/parent    | Iteratively list parent modules                                     |           |          |
+--------------------------+---------------------------------------------------------------------+-----------+----------+





