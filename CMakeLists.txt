cmake_minimum_required(VERSION 3.10)

# allow modern c++ feature from c++11 or later
set(CMAKE_CXX_STANDARD 11)

project(ChuckNorris)

add_library(sqlite3 STATIC IMPORTED)

set_target_properties(sqlite3
    PROPERTIES
    IMPORTED_LOCATION $HOME/3rdpart/sqlite/sqlite-amalgamation-3350200/lib/libsqlite3.a
    INTERFACE_INCLUDE_DIRECTORIES $HOME/3rdpart/sqlite/sqlite-amalgamation-3350200/include
)

# declare dependant libs from sqlite3 on linux
if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
  set_target_properties(sqlite3
    PROPERTIES
      INTERFACE_LINK_LIBRARIES "dl;pthread"
   )
endif()

# describe the first build target
add_library(chucknorris
    include/ChuckNorris.hpp
    src/ChuckNorris.cpp
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

# say that cpp_demo depends on chucknorris
target_link_libraries(cpp_demo chucknorris)

# say that chucknorris depends on sqlite
target_link_libraries(chucknorris sqlite3)