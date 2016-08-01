git clone https://github.com/MacPython/terryfy.git
source terryfy/library_installers.sh
clean_builds
get_python_environment macpython $VERSION venv
pip install --upgrade pip wheel
pip install -r dev-requirements.txt