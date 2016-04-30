#!/bin/bash
set -e -x

cd /io

# test and compile wheels
for PYBIN in /opt/python/*/bin/; do
    ${PYBIN}/pip install -r /io/dev-requirements.txt
    ${PYBIN}/python setup.py test
    ${PYBIN}/pip wheel /io/ -w /tmp/wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in /tmp/wheelhouse/bencoder*.whl; do
    auditwheel repair $whl -w /io/wheelhouse/
done
