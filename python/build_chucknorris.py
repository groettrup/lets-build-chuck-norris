from cffi import FFI
import json
import path
# add path definitions
cpp_path = path.Path("../cpp").abspath()
cpp_build_path = cpp_path.joinpath("build/default")
ck_lib_path = cpp_build_path.joinpath("lib/chucknorris.lib")
ck_include_path = cpp_path.joinpath("include")

extra_objects=[ck_lib_path]
include_dirs=[ck_include_path, cpp_build_path]

conan_info = json.loads(cpp_build_path.joinpath("conanbuildinfo.json").text())
for dep in conan_info["dependencies"]:
    for lib_name in dep["libs"]:
        lib_filename = "%s.lib" % lib_name
        for lib_path in dep["lib_paths"]:
            candidate = path.Path(lib_path).joinpath(lib_filename)
            if candidate.exists():
                extra_objects.append(candidate)
            else:
                libraries.append(candidate)
    for include_path in dep["include_paths"]:
        include_dirs.append(include_path)
ffibuilder = FFI()

ffibuilder.set_source(
    "_chucknorris",
    """
    #include <chucknorris.h>
    """,
    extra_objects=extra_objects,
    include_dirs=include_dirs,
    libraries=["msvcrtd"],
)

ffibuilder.cdef("""
typedef struct chuck_norris chuck_norris_t;
chuck_norris_t* chuck_norris_init(void);
const char* chuck_norris_get_fact(chuck_norris_t*);
void chuck_norris_deinit(chuck_norris_t*);
""")