import os.path
import sys
import platform

from setuptools import setup
from setuptools.extension import Extension

version = platform.python_version_tuple()
install_requires = []
if version < ('2', '7'):
    install_requires.append('ordereddict>=1.1')

base_path = os.path.dirname(os.path.abspath(__file__))
pyx_path = os.path.join(base_path, 'bencoder.pyx')
c_path = os.path.join(base_path, 'bencoder.c')

if sys.argv[-1] == 'test' and platform.python_implementation() == 'CPython':
    from Cython.Compiler.Options import directive_defaults

    directive_defaults['linetrace'] = True
    directive_defaults['binding'] = True

    from Cython.Build import cythonize
    ext_modules = cythonize(Extension(
        "bencoder",
        [pyx_path],
        define_macros=[('CYTHON_TRACE', '1')] 
    ))
elif os.path.exists(c_path):
    ext_modules = [Extension(
        'bencoder',
        [c_path]
    )]
else:
    from Cython.Build import cythonize
    ext_modules = cythonize(Extension(
        "bencoder",
        [pyx_path]
    ))


# patch bdist_wheel
cmdclass = {}
try:
    from wheel.bdist_wheel import bdist_wheel

    REPLACE = (
        'macosx_10_6_intel.'
        'macosx_10_9_intel.'
        'macosx_10_9_x86_64.'
        'macosx_10_10_intel.'
        'macosx_10_10_x86_64'
    )

    class _bdist_wheel(bdist_wheel):
        def get_tag(self):
            tag = bdist_wheel.get_tag(self)
            if tag[2] == 'macosx_10_6_intel':
                tag = (tag[0], tag[1], REPLACE)
            return tag

    cmdclass['bdist_wheel'] = _bdist_wheel
except ImportError:
    pass


setup(
    name='bencoder.pyx',
    version='1.1.2',
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
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=['cython', 'pytest', 'pytest-cov'],
)
