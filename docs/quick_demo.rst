.. _quick_demo:


***************
Quick demo
***************

Install Docker
==============
You need to have Docker installed. Docker is a new container technology (Think of it as a light-weight virtualbox). Instructions for installation can be found here::

  https://docs.docker.com/installation/

Setting up the environment for simS2E
=====================================

You need to clone the simS2E repository from GitHub into your local directory (I will refer to this directory as /host/path)::

  git clone https://github.com/chuckie82/simS2E.git

*TODO* copy pmi_out_0000001.h5 to /host/path/simS2E/data/sim_example/pmi

Go to the location of the Dockerfile::
  
  cd /host/path/simS2E/packages/singfel

Build the SingFEL Dockerfile::

  docker build -t chuckie82/sims2e_singfel:v1 .

Now you are ready to run the simulation!!!

Run the SingFEL docker image::

  docker run -it -v /host/path/simS2E:/simS2E chuckie82/sims2e_singfel:v1 /bin/bash

You are now inside the Docker container running Ubuntu v14.04. The simulation is located under /data/S2E.

Go to the workflow directory and run the simple example::

  cd /data/S2E/workflow
  ./runSingFEL

When the simulation is complete. Exit the docker container by typing "exit".
The diffraction file will be in /host/path/simS2E/data/sim_example/diffr

You can examine the hdf5 file by running::

  cd /host/path/s2eDocs/modules/diffr
  python diagnostic_singfel.py /host/path/simS2E/data/sim_example

You should observer two matplotlib plots: 1) photon filed and 2) photon count. You may need to install h5py, matplotlib and numpy to run this script.



