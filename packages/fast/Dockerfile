FROM ubuntu:14.04

MAINTAINER Alexey Buzmakov <buzmakov@gmail.com>

###################
# Setup environment
###################
ENV ROOT_DIR /home
RUN mkdir -p $ROOT_DIR

###################
# Install packages
###################
ENV PYTHON_MAJOR 2
ENV PYTHON_MINOR 7
RUN apt-get update && apt-get install -y \
    build-essential gfortran \
    python${PYTHON_MAJOR}.${PYTHON_MINOR}-dev \
    unzip python-numpy python-scipy python-h5py \ 
    wget nano && apt-get clean && apt-get autoclean

###################
# Install WPG
###################
RUN mkdir -p $ROOT_DIR/packages && cd $ROOT_DIR/packages && \
    wget http://github.com/samoylv/WPG/archive/develop.zip -O wpg-develop.zip && \
    unzip wpg-develop.zip && mv WPG-develop WPG && rm wpg-develop.zip && \
    cd WPG && make all && rm -rf build
    
###################
# Install FEL
###################
RUN mkdir -p $ROOT_DIR/modules && cd $ROOT_DIR/modules && wget https://github.com/samoylv/FELsource/archive/master.zip -O FELsource-master.zip && \
    unzip FELsource-master.zip && mv FELsource-master FELsource && \
    cd FELsource && gfortran -ffixed-line-length-132 pproc-fast2xy-2013-v2-06-wo-fname.for -o pproc-fast2xy-2013-v2-06-wo-fname.exe && \
    mkdir -p $ROOT_DIR/data/FELsource && \
    wget http://dcache-door-photon03.desy.de:2980/simS2E/FELsource/3fs_20/FELsource_out_0000001.h5 -O FELsource_out_0000001.h5

###################
# Setup directories
###################
#RUN cd $ROOT_DIR && \
#    ln -s $ROOT_DIR/workflow workflow && \
#    ln -s $ROOT_DIR/config config && \
#    ln -s $ROOT_DIR/data data && \
##    ln -s /simS2E/modules modules && \
#    ln -s $ROOT_DIR/tmp tmp
