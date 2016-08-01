#!/bin/bash
sudo pip install twine
sudo twine upload --username whtsky --password $PYPI_PASSWORD wheelhouse/bencoder*.whl