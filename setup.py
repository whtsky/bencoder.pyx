import os.path
import sys
import os

from setuptools import setup
from setuptools.extension import Extension
from setuptools.command.test import test as TestCommand

pyx_path = 'bencoder.pyx'
c_path = 'bencoder.c'

if os.path.exists(c_path):
    # Remove C file to force Cython recompile.
    os.remove(c_path)

if os.environ.get("BENCODER_LINETRACE", "") == "1":
    from Cython.Compiler.Options import get_directive_defaults
    directive_defaults = get_directive_defaults()

    directive_defaults['linetrace'] = True
    directive_defaults['binding'] = True

from Cython.Build import cythonize
ext_modules = cythonize(Extension(
    "bencoder",
    [pyx_path],
    extra_compile_args=['-O3']
))


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import coverage
        cov = coverage.Coverage()
        cov.start()

        import pytest
        errno = pytest.main(self.pytest_args)

        cov.stop()
        cov.save()
        sys.exit(errno)


cmdclass = {'test': PyTest}



setup(
    name='bencoder.pyx',
    version='3.0.1',
    description='Yet another bencode implementation in Cython',
    long_description=open('README.rst', 'r').read(),
    author='whtsky',
    author_email='whtsky@gmail.com',
    url='https://github.com/whtsky/bencoder.pyx',
    license='BSDv3',
    platforms=['POSIX', 'Windows'],
    zip_safe=False,
    include_package_data=True,
    keywords=['bencoding', 'encode', 'decode', 'bittorrent', 'bencode', 'bencoder', 'cython'],
    cmdclass=cmdclass,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    ext_modules=ext_modules,
    install_requires=[],
    tests_require=['cython', 'pytest', 'coverage'],
)
