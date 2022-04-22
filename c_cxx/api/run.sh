#!/bin/bash -xe

ONNXRUNTIME_ROOTDIR=/home/azureuser/cloudfiles/data/Users/nakersha/lib/onnxruntime-linux-x64-gpu-1.11.0
export LD_LIBRARY_PATH=${ONNXRUNTIME_ROOTDIR}/lib
export LIBRARY_PATH=${ONNXRUNTIME_ROOTDIR}/lib
rm -rf build
mkdir build
cd build
cmake .. -DONNXRUNTIME_ROOTDIR=${ONNXRUNTIME_ROOTDIR}
cmake --build .
