#!/usr/bin/env bash
cython bencoder.pyx
python setup.py sdist --formats=zip,gztar register
tox -c tox-wheels.ini
twine upload dist/*
