FROM ubuntu:14.04

MAINTAINER Chunhong Yoon <chuckie82@gmail.com>

###################
# Setup environment
###################

ENV LIB_DIR /data/S2E/lib/diffr
RUN mkdir -p $LIB_DIR
ENV DIFFR_DIR /data/S2E/packages/diffr
RUN mkdir -p $DIFFR_DIR

###################
# Install packages
###################
ENV PYTHON_MAJOR 2
ENV PYTHON_MINOR 7
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    cmake \
    python${PYTHON_MAJOR}.${PYTHON_MINOR}-dev \
    python-h5py \
    libbz2-dev \
    git \
    libgsl0-dev

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
# Install SingFEL
###################
RUN cd $DIFFR_DIR && \
    wget https://www.dropbox.com/s/nnoc78iafor0qrn/singfel.tar.gz?dl=0 -O singfel.tar.gz && \
    mkdir singfel && \
    tar -xvf singfel.tar.gz -C singfel --strip-components 1 && \
    rm singfel.tar.gz && \
    cd singfel && \
    mkdir build && cd build && \
    cmake

###################
# Setup directories
###################
RUN ln -s /simS2E/workflow workflow && \
    ln -s /simS2E/config config && \
    ln -s /simS2E/data data && \
    ln -s /simS2E/modules modules && \
    ln -s /simS2E/tmp tmp

