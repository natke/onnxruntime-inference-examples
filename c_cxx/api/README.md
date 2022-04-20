# ONNX Runtime C++ API example

## Pre-requisites

Download ONNX Runtime zip

## Build

rm -rf build
mkdir build
cd build
cmake .. -DONNXRUNTIME_ROOTDIR=<location of ONNX Runtime installation>
cmake --build .
