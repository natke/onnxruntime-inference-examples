rm -rf build
mkdir build
cd build
cmake .. -DONNXRUNTIME_ROOTDIR=/c/Users/nakersha/Develop/lib/onnxruntime-win-x64-1.11.0
cmake --build .
