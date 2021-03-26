from setuptools import setup

setup(
    name="chucknorris",
    version="0.1.0",
    description="chucknorris python bindings",
    author="alexander gröttrup",
    py_modules=["chucknorris"],
    setup_requires=["cffi","path.py"],
    cffi_modules=["build_chucknorris.py:ffibuilder"],
    install_requires=["cffi"],
)