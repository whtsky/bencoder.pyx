#!/bin/bash
set -e -x

# test and compile wheels
for PYBIN in /opt/python/*/bin/; do
    ${PYBIN}/pip install -r /io/dev-requirements.txt
    ${PYBIN}/python /io/setup.py test
    ${PYBIN}/pip wheel /io/ -w wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/bencoder*.whl; do
    auditwheel repair $whl -w /io/wheelhouse/
done

