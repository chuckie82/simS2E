.. _coherent_diffraction:

.. image:: _static/detector.png
    :scale: 33 %

=================
Coherent Diffraction
=================

Input/Output data description
-----------------

The input/output data is expected in hdf5 format, and the glossary can be found below. Coherent diffraction module is responsible for reading in and writing out in the format specified below.

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+
