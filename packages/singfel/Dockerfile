FROM ubuntu:14.04

MAINTAINER Chunhong Yoon <chuckie82@gmail.com>

###################
# Setup environment
###################
ENV ROOT_DIR /data/S2E
RUN mkdir -p $ROOT_DIR
ENV LIB_DIR ${ROOT_DIR}/lib/diffr
RUN mkdir -p $LIB_DIR
ENV DIFFR_DIR ${ROOT_DIR}/packages/diffr
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
    libgsl0-dev \
    nano

###################
# Install MPICH
###################
ENV MPICH_MAJOR 3
ENV MPICH_MINOR 1
ENV MPICH_BUILD 2
RUN cd ${LIB_DIR} && \
    wget http://www.mpich.org/static/downloads/${MPICH_MAJOR}.${MPICH_MINOR}.${MPICH_BUILD}/mpich-${MPICH_MAJOR}.${MPICH_MINOR}.${MPICH_BUILD}.tar.gz && \
    tar -xvf mpich-${MPICH_MAJOR}.${MPICH_MINOR}.${MPICH_BUILD}.tar.gz && \
    rm mpich-${MPICH_MAJOR}.${MPICH_MINOR}.${MPICH_BUILD}.tar.gz && \
    cd ${LIB_DIR}/mpich-${MPICH_MAJOR}.${MPICH_MINOR}.${MPICH_BUILD} && \
    ./configure --disable-fortran --prefix=${LIB_DIR}/mpich-install 2>&1 | tee c.txt && \
    make 2>&1 | tee m.txt && \
    make install 2>&1 | tee mi.txt
ENV PATH ${LIB_DIR}/mpich-install/bin:$PATH

###################
# Install ARMADILLO
###################
ENV ARMA_VERSION 4.600.4
RUN cd ${LIB_DIR} && \
    wget http://sourceforge.net/projects/arma/files/armadillo-${ARMA_VERSION}.tar.gz && \
    tar -xvf armadillo-${ARMA_VERSION}.tar.gz && \
    rm armadillo-${ARMA_VERSION}.tar.gz && \
    cd ${LIB_DIR}/armadillo-${ARMA_VERSION} && \
    sed -i -e '12 s/^/ \/\/ /' ${LIB_DIR}/armadillo-${ARMA_VERSION}/include/armadillo_bits/config.hpp && \
    sed -i -e '19 s/^/ \/\/ /' ${LIB_DIR}/armadillo-${ARMA_VERSION}/include/armadillo_bits/config.hpp && \
    cmake . && \
    make install DESTDIR=${LIB_DIR}/armadillo-${ARMA_VERSION}
ENV ARMA_DIR ${LIB_DIR}/armadillo-${ARMA_VERSION}

###################
# Install BOOST
###################
ENV BOOST_MAJOR 1
ENV BOOST_MINOR 57
ENV BOOST_BUILD 0
RUN cd ${LIB_DIR} && \
    wget http://sourceforge.net/projects/boost/files/boost/${BOOST_MAJOR}.${BOOST_MINOR}.${BOOST_BUILD}/boost_${BOOST_MAJOR}_${BOOST_MINOR}_${BOOST_BUILD}.tar.gz && \
    tar -xvf boost_${BOOST_MAJOR}_${BOOST_MINOR}_${BOOST_BUILD}.tar.gz && \
    rm boost_${BOOST_MAJOR}_${BOOST_MINOR}_${BOOST_BUILD}.tar.gz && \
    cd ${LIB_DIR}/boost_${BOOST_MAJOR}_${BOOST_MINOR}_${BOOST_BUILD} && \
    ./bootstrap.sh --prefix=${LIB_DIR}/boost_${BOOST_MAJOR}_${BOOST_MINOR}_${BOOST_BUILD} --with-python=/usr/bin/python${PYTHON_MAJOR}.${PYTHON_MINOR} && \
    echo "using mpi ;" >> project-config.jam && \
    ./b2 install
ENV BOOST_DIR ${LIB_DIR}/boost_${BOOST_MAJOR}_${BOOST_MINOR}_${BOOST_BUILD}

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
    cmake .. && \
    make

###################
# Setup directories
###################
RUN cd $ROOT_DIR && \
    ln -s /simS2E/workflow workflow && \
    ln -s /simS2E/config config && \
    ln -s /simS2E/data data && \
    ln -s /simS2E/modules modules && \
    ln -s /simS2E/tmp tmp
