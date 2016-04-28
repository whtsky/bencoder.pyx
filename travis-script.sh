if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    python setup.py test
    pip wheel . -w wheelhouse/  
else
    docker run --rm -v `pwd`:/io $DOCKER_IMAGE $PRE_CMD /io/travis/build-wheels.sh
fi

