python setup.py test
bash <(curl -s https://codecov.io/bash)
rm bencoder.c
pip wheel . -w wheelhouse/