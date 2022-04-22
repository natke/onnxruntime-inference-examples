cmake_minimum_required(VERSION 3.10)

option(ONNXRUNTIME_ROOTDIR "onnxruntime root dir")

# set the project name
project(api VERSION 0.0.1)

# add include directory
include_directories( 
    ${ONNXRUNTIME_ROOTDIR}/include
)

# add the executable
add_executable(api_app main.cpp)
target_link_libraries(api_app onnxruntime)

