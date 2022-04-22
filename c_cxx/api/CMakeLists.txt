cmake_minimum_required(VERSION 3.10)

option(ONNXRUNTIME_ROOTDIR "onnxruntime root dir")

include_directories( 
    ${ONNXRUNTIME_ROOTDIR}/include
)

# set the project name
project(api VERSION 0.0.1)

# add the executable
add_executable(api_app main.cpp)
target_link_libraries(api_app onnxruntime)


