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

System requirements
===================
You will need at least 8GB RAM and 20GB of disk space.

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

Go to the workflow directory and run the example. This will generate a single FEL pulse::

  cd /simS2E/workflow
  ./runFAST

This script runs master.sh which in turn runs master_fast.sh. All the simulation configuration is defined in /simS2E/config/config_sim_example. Let's examine the configuration file::

  nano /simS2E/config/config_sim_example

NUM_FELsource_OUT=1 means output 1 instance of the FEL pulse.
FELsource=ppFAST means use the FAST package.
FAST simulation parameters are defined under ###### ppFAST ######.

When the simulation is complete. Exit the docker container by typing "exit" or Contrl+D.
FELsource output hdf5 file will be in /host/path/simS2E/data/sim_example/FELsource. You can examine the hdf5 file by running::

  h5ls -r /host/path/simS2E/data/sim_example/FELsource/FELsource_out_0000001.h5

Note that the output hdf5 names and fields conform to the specifications of the simS2E framework.

2 ) Let's run the optics simulation using WPG::

  docker run -it -v /host/path/simS2E:/simS2E wpg:v0.1 /bin/bash

You are now inside the Docker container running bash on Ubuntu v14.04. The WPG package is installed under /home/packages and the simS2E directory is located under /simS2E.

Go to the workflow directory and run the example. This will generate the FEL pulse that will hit the sample after propagating through the SPB/SFX beamline optics::

  cd /simS2E/workflow
  ./runWPG

When the simulation is complete. Exit the docker container by typing "exit" or Contrl+D.
WPG output hdf5 file will be in /host/path/simS2E/data/sim_example/prop.

3 ) Let's run the photon matter interaction simulation using PMI_DEMO::

  docker run -it -v /host/path/simS2E:/simS2E pmi_demo:v0.1 /bin/bash

You are now inside the Docker container running bash on Ubuntu v14.04. The PMI_DEMO package is installed under /home/packages and the simS2E directory is located under /simS2E. Due to the license agreement, the PMI package is not available in this example simulation and demo version is used instead.

Go to the workflow directory and run the example. This will generate the scattering factors of the sample under going radiation damage over time::

  cd /simS2E/workflow
  ./runPMI

The pdb file that specifies the initial atom positions and scattering factors is stored under /simS2E/data/sim_example/sample/sample.h5.
When the simulation is complete, exit the docker container by typing "exit" or Contrl+D.
PMI_DEMO output hdf5 file will be in /host/path/simS2E/data/sim_example/pmi.

4 ) Let's run the diffraction simulation using SingFEL::

  docker run -it -v /host/path/simS2E:/simS2E singfel:v0.1 /bin/bash

You are now inside the Docker container running bash on Ubuntu v14.04. The SingFEL package is installed under /home/packages and the simS2E directory is located under /simS2E.

Go to the workflow directory and run the example. This will generate the diffraction patterns of the sample under going radiation damage over time::

  cd /simS2E/workflow
  ./runSingFEL

Let's open the simulation configuration file again in /simS2E/config/config_sim_example. NUM_DIFFR_OUT=100 means generate 100 time evolution diffraction patterns. In order to run a meaningful simulation, try increasing this number to 50,000. DIFFR=singfel means use the SingFEL package. SingFEL parameters are defined under ###### SingFEL ######. When the simulation is complete, exit the docker container by typing "exit" or Contrl+D. SingFEL output hdf5 file will be in /host/path/simS2E/data/sim_example/pmi.

You can examine the hdf5 file by running::

  cd /host/path/s2eDocs/modules/diffr
  python diagnostic_singfel.py /host/path/simS2E/data/sim_example

You should observe two matplotlib plots: 1) photon field and 2) photon count. You may need to install h5py, matplotlib and numpy to run this script.

5 ) Let's run the orientation recovery simulation using EMC::

  docker run -it -v /host/path/simS2E:/simS2E emc:v0.1 /bin/bash

You are now inside the Docker container running bash on Ubuntu v14.04. The EMC package is installed under /home/packages and the simS2E directory is located under /simS2E.

Go to the workflow directory and run the example. This will generate the 3D diffraction volume after orientation recovery. Note that EMC may take many hours to converge to a solution. On my Linux box, it takes about a day::

  cd /simS2E/workflow
  ./runEMC

Let's open the simulation configuration file again in /simS2E/config/config_sim_example. ORIENT=EMC specifies the EMC algorithm for orientation recovery. The EMC parameters are defined under ###### EMC ######. When the simulation is complete, exit the docker container by typing "exit" or Contrl+D. EMC output hdf5 file will be in /host/path/simS2E/data/sim_example/orient.

6 ) Let's run the phase retrieval simulation using DM::

  docker run -it -v /host/path/simS2E:/simS2E dm:v0.1 /bin/bash

###### DM ######
You are now inside the Docker container running bash on Ubuntu v14.04. The DM package is installed under /home/packages and the simS2E directory is located under /simS2E.

Go to the workflow directory and run the example. This will generate the 3D electron density.::

  cd /simS2E/workflow
  ./runDM

Let's open the simulation configuration file again in /simS2E/config/config_sim_example. PHASE=DM specifies the Difference Map algorithm for phase retrieval. The DM parameters are defined under ###### DM ######. When the simulation is complete. Exit the docker container by typing "exit" or Contrl+D. DM output hdf5 file will be in /host/path/simS2E/data/sim_example/phase.

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




