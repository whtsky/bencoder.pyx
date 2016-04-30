import os.path
import platform

from setuptools import setup
from setuptools.extension import Extension

version = platform.python_version_tuple()
install_requires = []
if version < ('2', '7'):
    install_requires.append('ordereddict>=1.1')

base_path = os.path.dirname(os.path.abspath(__file__))

try:
    from Cython.Build import cythonize
    ext_modules = cythonize(os.path.join(base_path, "bencoder.pyx"))
except ImportError:
    ext_modules = [Extension(
        'bencoder',
        [os.path.join(base_path, 'bencoder.c')]
    )]


setup(
    name='bencoder.pyx',
    version='1.1.1',
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
    classifiers=[
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    ext_modules=ext_modules,
    install_requires=install_requires,
    tests_require=['nose'],
    test_suite='nose.collector',
)
