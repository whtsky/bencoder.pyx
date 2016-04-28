if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    source terryfy/library_installers.sh
    clean_builds
    get_python_environment macpython $VERSION venv
    pip install --upgrade pip wheel cython
else
    docker pull $DOCKER_IMAGE
fi