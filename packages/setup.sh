#!/bin/bash
PWD=`pwd`
echo $PWD
basepath=$PWD

echo "Building fast"
cd "$basepath/fast"
docker build -t fast:v0.2 .

echo "Building wpg"
cd "$basepath/wpg"
docker build -t wpg:v0.2 .

echo "Building pmi_demo"
cd "$basepath/pmi_demo"
docker build -t pmi_demo:v0.2 .

echo "Building singfel"
cd "$basepath/singfel"
docker build -t singfel:v0.2 .

echo "Building EMC"
cd "$basepath/emc"
docker build -t emc:v0.2 .

echo "Building DM"
cd "$basepath/dm"
docker build -t dm:v0.2 .
