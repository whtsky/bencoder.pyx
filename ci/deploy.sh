#!/bin/bash
pip install twine
twine upload --username whtsky --password $PYPI_PASSWORD wheelhouse/bencoder*.whl