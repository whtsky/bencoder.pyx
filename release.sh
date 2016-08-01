#!/usr/bin/env bash
rm -rf wheelhouse/
rm -rf dist/
cython bencoder.pyx
python setup.py sdist --formats=zip,gztar register
tox -c tox-wheels.ini
twine upload dist/*
twine upload wheelhouse/*