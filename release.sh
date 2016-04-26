cython bencoder.pyx
python setup.py sdist --formats=zip,gztar bdist_wheel register
twine upload dist/*
