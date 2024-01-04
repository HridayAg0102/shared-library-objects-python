# setup.py

from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

sourceFiles = ["libcalculator/add.pyx",
               "libcalculator/subtract.pyx",
               "libcalculator/multiply.pyx",
               "libcalculator/divide.pyx"
               ]

extensions = cythonize([Extension(
             name="libcalculator." + source.split('/')[-1][:-4],  # Extract module name without '.pyx'
             sources=[source]
      ) for source in sourceFiles])

kwargs = {
    "name": "project",
    "version": "1.0",
    "packages": find_packages(),
    "ext_modules": extensions,
    "package_data": {'libcalculator': ['*.so']},
    "include_package_data": True
}

setup(**kwargs)
