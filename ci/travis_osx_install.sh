git clone https://github.com/matthew-brett/multibuild.git
source multibuild/osx_utils.sh
get_macpython_environment $VERSION venv
pip install --upgrade pip wheel
pip install -r dev-requirements.txt