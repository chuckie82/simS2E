FROM ubuntu:14.04

MAINTAINER Chunhong Yoon <chuckie82@gmail.com>

###################
# Setup environment
###################
ENV ROOT_DIR /data/S2E
RUN mkdir -p $ROOT_DIR
ENV LIB_DIR ${ROOT_DIR}/lib/orient
RUN mkdir -p $LIB_DIR
ENV PKG_DIR ${ROOT_DIR}/packages/orient
RUN mkdir -p $PKG_DIR

###################
# Install packages
###################
ENV PYTHON_MAJOR 2
ENV PYTHON_MINOR 7
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    python${PYTHON_MAJOR}.${PYTHON_MINOR}-dev \
    python-h5py \
    python-matplotlib \
    python-setuptools \
    python-scipy \
    cython \
    nano

###################
# Install HDF5
###################
ENV HDF5_MAJOR 1
ENV HDF5_MINOR 8
ENV HDF5_BUILD 9
RUN cd $LIB_DIR && \
    wget http://www.hdfgroup.org/ftp/HDF5/releases/hdf5-${HDF5_MAJOR}.${HDF5_MINOR}.${HDF5_BUILD}/src/hdf5-${HDF5_MAJOR}.${HDF5_MINOR}.${HDF5_BUILD}.tar.gz && \
    tar -xvf hdf5-${HDF5_MAJOR}.${HDF5_MINOR}.${HDF5_BUILD}.tar.gz && \
    rm hdf5-${HDF5_MAJOR}.${HDF5_MINOR}.${HDF5_BUILD}.tar.gz && \
    cd hdf5-${HDF5_MAJOR}.${HDF5_MINOR}.${HDF5_BUILD} && \
    ./configure --prefix=${LIB_DIR}/hdf5-${HDF5_MAJOR}.${HDF5_MINOR}.${HDF5_BUILD} --enable-cxx && \
    make install
ENV HDF5_DIR ${LIB_DIR}/hdf5-${HDF5_MAJOR}.${HDF5_MINOR}.${HDF5_BUILD}

###################
# Install EMC
###################
RUN cd $PKG_DIR && \
    wget https://db.tt/8CTthFkw -O s2e_recon.tar.gz && \
    mkdir s2e_recon && \
    tar -xvf s2e_recon.tar.gz -C s2e_recon --strip-components 1 && \
    rm s2e_recon.tar.gz && \
    cd s2e_recon

###################
# Setup directories
###################
RUN cd $ROOT_DIR && \
    ln -s /simS2E/workflow workflow && \
    ln -s /simS2E/config config && \
    ln -s /simS2E/data data && \
    ln -s /simS2E/modules modules && \
    ln -s /simS2E/tmp tmp
