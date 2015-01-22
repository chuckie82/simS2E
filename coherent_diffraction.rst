.. _coherent_diffraction:

.. image:: _static/detector_rsz.png
    :scale: 100 %

Coherent Diffraction
====================

Input/Output data description
-----------------------------

The input/output data is expected in hdf5 format, and the glossary can be found below. Coherent diffraction module is responsible for reading in and writing out in the format specified below.

diffr_params_SingFEL (Input Parameter glossary)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

==================  ==========================================================  ==========
Field name          Description                                                 DataType
==================  ==========================================================  ==========
--input_dir         Input directory where pmi_out files are stored              String
--output_dir        Output directory where diffr_out files will be stored       String
--config_file       Full path and filename of this file                         String 	 
-b                  Experimental beam file                                      String 	 
-g                  Experimental geometry file                                  String 	 
--uniformRotation   Rotations are selected uniformly in given rotation space    Int
--calculateCompton  Calculate Compton scattering in diffraction pattern         Int
--sliceInterval     Interval to calculates diffraction                          Int 	 
--numSlices         Number of time slices to use for calculating diffraction    Int 	 
--pmiStartID        Start ID of PMI trajectory                                  Int 	 
--pmiEndID          End ID of PMI trajectory                                    Int 	 
--dpID              Diffraction pattern index for current pmiID                 Int 	 
--numDP             Number of diffraction patterns to generate per pmiID        Int 	 
--USE_GPU           Options to use GPU (1) or not (0)                           Int  	 
version             SingFEL version                                             0.1
==================  ==========================================================  ==========

diffr_out_<7 digit ID>.h5 (Output HDF glossary)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| Field name               | Description                                                         | Data type | Units     |
+==========================+=====================================================================+===========+===========+
| **data/**                |                                                                     |           |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| data/data                | Diffraction pattern in 2D matrix |                                  | Float     |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| data/diffr               | Diffracted intensity before Poisson noise (Optional)                | Float     |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| data/angle               | Additional rotation applied to the rotated pmi_out position.        |           |           |
|                          | Initial rotation angle can be found in pmi_out/data/angle.          | Float     |           |
|                          | Active right handed rotations applied in quaternion.                |           |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| **history/**             | Information about input data                                        |           |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| history/parent/detail    | Details of the parent including /data, /info, /misc, /params        |           |           |
|                          | /data should be soft-linked with a relative path                    |           |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| history/parent/parent    | Iteratively list parent modules                                     |           |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| **info/**                | Information                                                         |           |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| info/package_version     | Package name and version                                            | String    |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| info/contact             | Contact details of author                                           | String    |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| info/data_description    | Short description of what the data is                               | String    |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| info/method_description  | Short description of what method was used to generate the data      | String    |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| **misc/**                | Miscellaneous information                                           |           |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| **params/**              | Parameters used for coherent diffraction                            |           |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| params/geom/detectorDist | Detector distance from point of interaction                         | Float     | m         |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| params/geom/pixelWidth   | Pixel width                                                         | Float     | m         |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| params/geom/pixelHeight  | Pixel height                                                        | Float     | m         |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| params/geom/mask         | Mask of a diffraction pattern to indicate                           | Int       |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
|                          | pixel ON (1) or OFF (0) in 2D array 		                 |           |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| params/beam/photonEnergy | Photon energy                                                       | Float     | eV        |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| params/beam/photons      | Number of photons in the beam                                       | Int       | ph        |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| params/beam/focusArea    | Beam focus area                                                     | Float     |:math:`m^2`|
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| params/info              | Input for Coherent diffraction program                              | String    |           |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+
| **version**              | hdf5 format version                                                 | Float     | 0.1       |
+--------------------------+---------------------------------------------------------------------+-----------+-----------+

Diagnostic
----------

Python script displays /data/data and /data/diffr at completion of the module execution.

 
Scaling behaviour of SingFEL
----------------------------

Calculation time using single processor vs number of atoms is non-linear, perhaps quadratic.

Detector number of pixels: 131x131

Benzoic acid: 15 atoms
Chignolin: 2484 atoms
2YBE: 3240 atoms
2NIP: 4735 atoms
4AS4: 4963 atoms

.. image:: _static/singfel_speed.png
    :scale: 100 %


