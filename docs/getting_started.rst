.. _getting_started:


***************
Getting started
***************

.. _installing-docdir:

.. image:: _static/pmi_rsz.png
    :scale: 100 %

simS2E is an implementation-agnostic framework that defines the data interfaces between the modules, i.e. Module A must output an hdf5 file that adheres to the simS2E interface which Module B is expecting to read in. Actual implementation of Modules A and B is up to the user. If you understand this concept, then you are ready to use simS2E. You will need to set up the environment for simS2E and if you have a module that you want to plug in, find out what data formats the input and output should be here::

  http://sims2e.readthedocs.org/en/latest/docs/fel_source_simulation.html

If you would like to try running an example simS2E pipeline, then you need Docker installed on your machine.

Installing Docker for example simS2E pipeline
=============================================
You do NOT need Docker for simS2E. You only need it for running the example simS2E pipeline that we provide. Docker is a new container technology (Think of it as a light-weight virtualbox) that can be run on your choice of OS. Instructions for installation can be found here::

  https://docs.docker.com/installation/

Setting up the environment for simS2E
=====================================

You need to clone the simS2E repository from GitHub into your local directory (I will refer to this directory as /host/path)::

  cd /host/path
  git clone https://github.com/chuckie82/simS2E.git

You now have a copy of all the files/scripts in the sub-directories needed for simS2E::

  /host/path/simS2E/workflow: Directory for run scripts
  /host/path/simS2E/config: Directory for configuration files
  /host/path/simS2E/data: Directory for reading/saving data
  /host/path/simS2E/packages: Directory for installing software packages
  /host/path/simS2E/modules: Directory for module specific scripts
  /host/path/simS2E/tmp: Directory for storing temporary files
  /host/path/simS2E/docs: Directory for online documentation

Go to the packages directory and run setup.sh. This will build all the packages as Docker containers; 1) FAST for FEL source, 2) WPG for optics, 3) pmi_demo for radiation damage to the sample, 4) SingFEL for diffraction patterns, 5) EMC for orientation recovery, and 6) DM for phase retrieval::
  
  cd /host/path/simS2E/packages
  ./setup.sh

Now you are ready to run the simulation!!!

1 ) Let's run the FEL source simulation using FAST::

  docker run -it -v /host/path/simS2E:/simS2E fast:v0.1 /bin/bash

You are now inside the Docker container running bash on Ubuntu v14.04. The FAST package is installed under /home/packages and the simS2E directory is located under /simS2E.

Go to the workflow directory and run the simple example::

  cd /simS2E/workflow
  ./runFAST

When the simulation is complete. Exit the docker container by typing "exit" or Contrl+D.
The FELsource output hdf5 file will be in /host/path/simS2E/data/sim_example/FELsource



You can examine the hdf5 file by running::

  cd /host/path/s2eDocs/modules/diffr
  python diagnostic_singfel.py /host/path/simS2E/data/sim_example

You should observer two matplotlib plots: 1) photon field and 2) photon count. You may need to install h5py, matplotlib and numpy to run this script.

Setting up Sphinx for documenting simS2E simulation
=================================================================

You need clone the simS2E repository from GitHub::

  git clone https://github.com/chuckie82/start-to-end.git

The index.rst is the master ReST for your project.

You may already have `sphinx <http://sphinx.pocoo.org/>`_
installed -- you can check by doing::

  python -c 'import sphinx'

If that fails install the latest version with::

  > sudo easy_install -U Sphinx

Let's see if we can build our html::

  make html

If you now open your favorite internet browser and type :file:`_build/html/index.html`, you
should see the documentation website.

To update the document on the web, just push your changes::

   git add *.rst
   git commit -m "Update all documents"
   git push -u origin master

That's it! Now you are ready to 

.. image:: _static/undulator_rsz.png
    :scale: 100 %




