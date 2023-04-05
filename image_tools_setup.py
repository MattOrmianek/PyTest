from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("image_tools.pyx")
)