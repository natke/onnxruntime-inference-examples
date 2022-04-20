cmake_minimum_required(VERSION 3.10)

option(ONNXRUNTIME_ROOTDIR "onnxruntime root dir")

# set the project name
project(api)

# add the executable
add_executable(api_app main.cpp)
