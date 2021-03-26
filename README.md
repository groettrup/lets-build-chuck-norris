# lets-build-chuck-norris

Repository that follows the blog posts [Introducing the "Let's Build Chuck Norris!" Project](https://dmerej.info/blog/post/introducing-the-chuck-norris-project/)
from [Dimitri Merejkowsky](https://dmerej.info/blog/pages/about/) :

> “Let’s Build Chuck Norris!” is a series of blog posts aiming at exploring various topics about
> C++ and build systems, and providing an example of the Salami method described by Adi Shavit.

## Setting up ninja in VS Code

For this project I am using VS Code with the [_CMake Tools 1.6.0_ extension from Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

The Guide only uses ninja and cmake in the first blog post. In the build folder a default folder is used to configure cmake in.
Cmake is configured by runnin `cmake -GNinja ../..` from the folder called _default_. the cmake extension is also used to generate
the _compile\_commands.json_ file, which is required by clangd to find libraries.  

The right generator and build directory can be changed in the CMake Extensions in VSCode:

|      Setting ID      |                 Value                  |
|:---------------------|:---------------------------------------|
|`cmake.buildDirectory`|`${workspaceFolder}/build/default`      |
|`cmake.generator`     |`Ninja`                                 |
|`cmake.configureArgs` |`["-DCMAKE_EXPORT_COMPILE_COMMANDS=ON"]`|

## Downloading SQLite

For the manual download, I am using an updated version of
sqlite3 with the link https://www.sqlite.org/2021/sqlite-amalgamation-3350200.zip

with llvm-ar the _f_ option is not available anymore

## Using Conan to handle dependencies

The sqlite3 dependency had to be build locally, because the clang package is not
prebuilt. The default generator for cmake on Windows is "MinGW Makefiles". To use
Ninja, the environment variable _CONAN_CMAKE_GENERATOR_ can be used. This can be
enabled for conan with the addition to `%USERPROFILE%\.conan\profiles\default`:

```ini
...
[env]
CONAN_CMAKE_GENERATOR=Ninja
```

## Building the Shared Library
on windows the build just works, because the _sqlite3_ is already built with all
Options enabled. The generated DLL is missing all symbols to link. _cmake_ has a
macro that generates macros in a header file called _chucknorris_Export.h_ in this
case to mark certain functions as functions that should be exported.

The module that provides this macro can be included using the following lines:
```cmake
include(GenerateExportHeader)
GENERATE_EXPORT_HEADER(chucknorris)
```

the header file is generated in the _build/default_ folder, which can be included
using `$<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>` in the include directories
macro for the library.

VS Code also passed the option `-DBUILD_SHARED_LIBS=ON` to cmake to set the library
as _SHARED_

## Creating a Python Wheel
The current build environment uses _msvcrtd_ as standard library to use it in python
as well, we need to add the option `libraries=["msvcrtd"],` to the _set\_source_
command in _build_chucknorris.py_