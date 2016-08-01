#!/bin/bash
set -e -x

cd /io

# compile wheels
for PYBIN in /opt/python/*/bin/; do
    ${PYBIN}/pip install cython
    ${PYBIN}/pip wheel /io/ -w /tmp/wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in /tmp/wheelhouse/bencoder*.whl; do
    auditwheel repair $whl -w /io/wheelhouse/
done

cp /tmp/wheelhouse/ordereddict* /io/wheelhouse

# Install packages and test again
for PYBIN in /opt/python/*/bin/; do
    ${PYBIN}/pip install bencoder.pyx --no-index -f /io/wheelhouse
    ${PYBIN}/pip install pytest
    (cd /io; ${PYBIN}/py.test -c pytest-nocov.ini)
done
