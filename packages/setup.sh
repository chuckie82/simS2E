#!/bin/bash
PWD=`pwd`
echo $PWD
basepath=$PWD

echo "Buiding fast"
cd "$basepath/fast"
docker build -t fast:v0.1 .

echo "Buiding wpg"
cd "$basepath/wpg"
docker build -t wpg:v0.1 .

echo "Buiding pmi_demo"
cd "$basepath/pmi_demo"
docker build -t pmi:v0.1 .

echo "Buiding singfel"
cd "$basepath/singfel"
docker build -t singfel:v0.1 .

echo "Buiding EMC"
cd "$basepath/s2e_recon/EMC_Src"
docker build -t emc:v0.1 .

echo "Buiding DM"
cd "$basepath/s2e_recon/DM_Src"
docker build -t dm:v0.1 .
