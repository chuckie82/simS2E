.. _fel_source_simulation:

.. image:: _static/undulator.png
    :scale: 33 %

=================
FEL source simulation
=================

Introduction
-----------------

Documentation for FEL source simulation can be found on this page.

Data access
-----------------

Data in archive can be exported using web browser. Initial FEL source can be downloaded from here:

`FEL source web site <http://dcache-door-photon03.desy.de:2980/>`_

with authentication (xfel/desy account)

`FEL source web site <https://dcache-door-photon03:2880/XFEL/2014/SIM/>`_

If you use this dataset, please acknowledge blah blah blah ...

Output data description
-----------------

The output data is expected in hdf5 format, and the glossary can be found below. FEL source module is responsible for writing out in the format specified below.


FELsource_out_<7 digit ID>.h5 (Output HDF glossary)
----------------------------------------------

+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| Field name               | Description                                                             | Data type | Units    |
+==========================+=========================================================================+===========+==========+
| **data/**                |                                                                         |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| data/arrEhor             | Complex EM field written in 4D array, horizontal polarization           | Float     |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| data/arrEver             | Complex EM field written in 4D array, vertical polarization             | Float     |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| **params/**              | Parameters for wavefront propagation                                    |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/nSlices      | Numbers of points vs photon energy/time for the pulse                   | Int       |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/nx           | Numbers of points, horizontal                                           | Int       |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/ny           | Numbers of points, vertical                                             | Int       |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/sliceMax     | Max value of time [s] or energy [ev] for pulse (fragment)               | Float     | s or ev  |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/sliceMin     | Min value of time [s] or energy [ev] for pulse (fragment)               | Float     | s or ev  |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/xMax         | Maximum of horizontal range                                             | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/xMin         | Minimum of horizontal range                                             | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/yMax         | Maximum of vertical range                                               | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/yMin         | Minimum of vertical range                                               | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/zCoord       | Longitudinal position, for FEL output data - length of active undulator |           | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Rx                | Instantaneous horizontal wavefront radius                               | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Ry                | Instantaneous vertical wavefront radius                                 | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/dRx               | Error of wavefront horizontal radius                                    | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/dRy               | Error of wavefront vertical radius                                      | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/nval              | complex electric field nval==2                                          | Int       |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/photonEnergy      | Average photon energy                                                   | Float     | ev       |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/wDomain           | Wavefront in time or frequency (photon energy) domain                   | String    |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/wEFieldUnit       | Electric field units, {sqrt(W/mm^2) (time domain), arbitrary}           | String    |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/wFloatType        | Electric field numerical type                                           | String    |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/wSpace            | R-space or Q-space wavefront presentation                               | String    |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/xCentre           | Horizontal transverse coordinates of wavefront instant 'source center'  | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/yCentre           | Vertical transverse coordinates of wavefront instant 'source center'    | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| **history/parent/info/** | **Information about input data**                                        |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| history/parent/info/     | Contact Information                                                     | String    |          |
| contact                  |                                                                         |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| history/parent/info/     | Description of FEL data                                                 | String    |          |
| data_description         |                                                                         |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| history/parent/info/     | Method description                                                      | String    |          |
| method_description       |                                                                         |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| history/parent/info/     | Package version                                                         | String    |          |
| package_version          |                                                                         |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| **misc/**                | **Complimentary information**                                               |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| history/parent/misc/     | FELsource_params_FAST2XY.txt used for post-processing FAST output       | String    |          |
| FAST2XY.DAT              |                                                                         |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| history/parent/misc/     | radial distribution of far field divergence                             | Float     |          |
| angular_distribution     |                                                                         |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| history/parent/misc/     | near field transverse FEL beam size (FWHM)                              | Float     |          |
| spot_size                |                                                                         |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| history/parent/misc/     | gain curve, dependence of FEL pulse energy (column 2) from number       | Float     |          |
| gain_curve               | of working point (column 0) and active undulator length z[cm] (column 1)|           |          |   
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| history/parent/misc/nzc  | number of working point defines active undulator length                 | Int       |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| history/parent/misc/     | FEL pulse temporal structure, instantaneous power P(\tau)               | Float     |          |
| temporal_struct          |                                                                         |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| **version**              | **hdf5 format version**                                                 | Float     | 0.1      |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+

Diagnostic (diagnostic_felsrc.py)
---------------------------------
Fig.1. Pulse irradiance XY map (number of photons per pixel), the title contains size of the pixel;

Fig.2. Pulse time structure, the title contains the pulse energy value. 


