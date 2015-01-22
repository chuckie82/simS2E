.. _propagation:

.. image:: _static/optics.png
    :scale: 33 %

=================
Propagation, including optics
=================

Input data description
----------------------

The input data is expected in hdf5 format, and the glossary can be found in the link below.

prop_out_XXXXXXX.h5 (Output HDF glossary)
-----------------------------------------

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
| params/Mesh/qxMax        | Maximum of horizontal frequency (If params/wSpace is Q-space)           |           | 1/m      |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/qxMin        | Minimum of horizontal frequency (If params/wSpace is Q-space)           |           | 1/m      |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/qyMax        | Maximum of vertical frequency (If params/wSpace is Q-space)             |           | 1/m      |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/qyMin        | Minimum of vertical frequency (If params/wSpace is Q-space)             |           | 1/m      |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/sliceMax     | Max value of time [s] or energy [ev] for pulse (fragment)               | Float     | s or ev  |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/sliceMin     | Min value of time [s] or energy [ev] for pulse (fragment)               | Float     | s or ev  |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Mesh/xMax         | Maximum of horizontal range (If params/wSpace is R-space)               | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/xMin              | Minimum of horizontal range (If params/wSpace is R-space)               | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/yMax              | Maximum of vertical range (If params/wSpace is R-space)                 | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/yMin              | Minimum of vertical range (If params/wSpace is R-space)                 | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/zCoord            | Longitudinal position, for FEL output data - length of active undulator | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/beamline/printout | (add description)                                                       |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Rx                | Instantaneous horizontal wavefront radius                               | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/Ry                | Instantaneous vertical wavefront radius                                 | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/dRx               | Error of wavefront horizontal radius                                    | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/dRy               | Error of wavefront horizontal radius                                    | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/nval              | complex electric field nval==2                                          | Int       |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/photonEnergy      | Average photon energy                                                   | Float     | ev       |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/wDomain           | Wavefront in time or frequency (photon energy) domain                   | String    |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/wEFieldUnit       | Electric field units,                                                   |           |          |
|                          | sqrt(Phot/s/0.1%BW/mm^2),                                               |           |          |
|                          | sqrt(W/mm^2) for time domain,                                           | String    |          |
|                          | sqrt(J/eV/mm^2) for frequency domain                                    |           |          |
|                          | arbitrary                                                               |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/wFloatType        | Electric field numerical type                                           | String    |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/wSpace            | R-space or Q-space wavefront presentation                               | String    |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/xCentre           | Horizontal transverse coordinates of wavefront instant 'source center'  | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| params/yCentre           | Vertical transverse coordinates of wavefront instant 'source center'    | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| **info/**                |                                                                         |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| info/package_version     | Package version                                                         |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| info/contact             | Contact details of author                                               |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| info/data_description    | Short description of what the data is                                   |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| info/method_description  | Short description of what method was used to generate the data          |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| **history**              | **Information about input data**                                        |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| **misc/**                | **Complimentary information**                                           |           |          |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| misc/xFWHM               | FWHM belong x-axis                                                      | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| misc/yFWHM               | FWHM belong y-axis                                                      | Float     | m        |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+
| **version**              | **hdf5 format version**                                                 | Float     | 0.1      |
+--------------------------+-------------------------------------------------------------------------+-----------+----------+

Diagnostic (diagnostic.py)
--------------------------
Fig.1. Pulse irradiance XY map (number of photons per pixel), the title contains size of the pixel;

Fig.2. Plot of pulse time structure before and after propagating, the title contains the propagated pulse energy value. 

About WPG
---------
WPG, WaveProperGator is an interactive simulation framework for coherent X-ray wavefront propagation. WPG provides intuitive interface to the `SRW library <https://github.com/ochubar/SRW>`_. The application examples oriented on `European XFEL <http://www.xfel.eu/>`_ design parameters.

`Online documentation page <http://wpg.readthedocs.org>`_
