#!/bin/bash
PWD=`pwd`
echo $PWD
basepath=$PWD

echo "Building fast"
cd "$basepath/fast"
docker build -t fast:v0.1 .

echo "Building wpg"
cd "$basepath/wpg"
docker build -t wpg:v0.1 .

echo "Building pmi_demo"
cd "$basepath/pmi_demo"
docker build -t pmi_demo:v0.1 .

echo "Building singfel"
cd "$basepath/singfel"
docker build -t singfel:v0.1 .

echo "Building EMC"
cd "$basepath/s2e_recon/EMC_Src"
docker build -t emc:v0.1 .

echo "Building DM"
cd "$basepath/s2e_recon/DM_Src"
docker build -t dm:v0.1 .
