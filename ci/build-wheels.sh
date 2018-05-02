#!/bin/bash
set -e -x

cd /work

MANYLINUX_PYTHON=$(echo ${CIRCLE_JOB} | cut -d"_" -f2)
ARCHITECTURE=$(echo ${CIRCLE_JOB} | cut -d"_" -f1 | cut -d"-" -f2)
PYBIN=/opt/python/${MANYLINUX_PYTHON}/bin
echo "MANYLINUX_PYTHON [${MANYLINUX_PYTHON}] ${ARCHITECTURE}"
if [ "$ARCHITECTURE" == "x86" ]
then
    echo "x86 architect, use linux32"
    PRE_CMD=linux32
fi
${PRE_CMD} ${PYBIN}/pip install -r /work/dev-requirements.txt
${PRE_CMD} ${PYBIN}/pip wheel /work/ -w /tmp/wheelhouse/

for whl in /tmp/wheelhouse/bencoder*.whl; do
    auditwheel repair $whl -w /work/wheelhouse/
done

# Install packages and test again
${PRE_CMD} ${PYBIN}/pip install bencoder.pyx --no-index -f /work/wheelhouse
(cd /work; ${PRE_CMD} ${PYBIN}/py.test)