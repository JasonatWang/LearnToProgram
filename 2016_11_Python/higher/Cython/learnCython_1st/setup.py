from distutils.core import setup
from Cython.Build import cythonize
setup(
    name="pythonCython",
    ext_modules=cythonize("pythonCython.pyx")
)