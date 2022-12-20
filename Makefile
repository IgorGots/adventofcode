VENV_NAME=.venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

all: venv


venv:
		test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME) && make _install

# you can use this undescore method for update environment by hands
_install:
		${PYTHON} -m pip install -r requirements.txt

