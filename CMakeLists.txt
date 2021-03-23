cmake_minimum_required(VERSION 3.10)

project(ChuckNorris)

# allow modern c++ feature from c++11 or later
set(CMAKE_CXX_STANDARD 11)

# Use conan to include libraries
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

# describe the first build target
add_library(chucknorris
    include/ChuckNorris.hpp
    include/chucknorris.h
    src/ChuckNorris.cpp
    src/c_wrapper.cpp
)

# there are header files in the include directory
# PRIVATE would mean that headers are only used to compile
# INTERFACE would mean that headers are only used by consumers
# more info: https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html
target_include_directories(
    chucknorris
    PUBLIC
        "include"
)

# describe the second build target
add_executable(cpp_demo
    src/main.cpp
)

# describe the build target for testing the c api
add_executable(c_demo
    src/main.c
)

# say that cpp_demo depends on chucknorris
target_link_libraries(cpp_demo chucknorris)

# say that c_demo depends on chucknorris
target_link_libraries(c_demo chucknorris)

# say that chucknorris depends on a CONAN PKG
target_link_libraries(chucknorris CONAN_PKG::sqlite3)