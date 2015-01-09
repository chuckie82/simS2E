.. _coherent_diffraction:

.. image:: _static/detector.png
    :scale: 33 %

=================
Coherent Diffraction
=================

Input/Output data description
-----------------

The input/output data is expected in hdf5 format, and the glossary can be found below. Coherent diffraction module is responsible for reading in and writing out in the format specified below.

+---------------+---------------------------------------------------------+----------+
| Field name    | Description                                             | DataType |
+===============+=========================================================+==========+
| --input_dir   | Input directory where pmi_out files are stored          | String   |
+---------------+---------------------------------------------------------+----------+
| --output_dir  | Output directory where diffr_out files will be stored   | String   |
+---------------+---------------------------------------------------------+----------+

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======
