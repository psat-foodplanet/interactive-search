# FIXME
PROJECT_NAME=??

# Specify the names of all executables to make.
PROG=update install format lint precommit check
.PHONY: ${PROG}

update:
	pip install --upgrade pip wheel
	pip install --upgrade -r requirements.txt

install:
	pip install --upgrade pip wheel
	pip install -r requirements.txt

format:
	black .
	isort .

lint:
	pytest ${PROJECT_NAME} --flake8 ## 코드 컨벤션 감지기

precommit: format

check: format lint