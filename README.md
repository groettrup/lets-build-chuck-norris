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

