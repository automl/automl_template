# These have been configured to only really run short tasks. Longer form tasks
# are usually completed in github actions.

NAME := AutoMLTemplate
PACKAGE_NAME := automl_template

DIR := ${CURDIR}
SOURCE_DIR := ${CURDIR}/${PACKAGE_NAME}
DIST := ${DIR}/dist
DOCDIR := ${DIR}/docs
INDEX_HTML := file://${DOCDIR}/html/build/index.html
TESTS_DIR := ${DIR}/tests
EXAMPLES_DIR := ${DIR}/examples

.PHONY: help install-dev check format pre-commit clean clean-doc clean-build build docs examples publish test

help:
	@echo "Makefile ${NAME}"
	@echo "* install-dev      to install all dev requirements and install pre-commit"
	@echo "* check            to check the source code for issues"
	@echo "* format           to format the code with black and isort"
	@echo "* pre-commit       to run the pre-commit check"
	@echo "* clean            to clean the dist and doc build files"
	@echo "* build            to build a dist"
	@echo "* docs             to generate and view the html files, checks links"
	@echo "* examples         to run and generate the examples"
	@echo "* publish          to help publish the current branch to pypi"
	@echo "* test             to run the tests"

PYTHON ?= python
CYTHON ?= cython
PYTEST ?= python -m pytest
CTAGS ?= ctags
PIP ?= python -m pip
MAKE ?= make
BLACK ?= black
ISORT ?= isort
PYDOCSTYLE ?= pydocstyle
MYPY ?= mypy
PRECOMMIT ?= pre-commit
FLAKE8 ?= flake8
install-dev:
	$(PIP) install -e ".[tests,examples,docs]"
	pre-commit install

check-black:
	$(BLACK) ${SOURCE_DIR} --check || :
	$(BLACK) ${EXAMPLES_DIR} --check || :
	$(BLACK) ${TESTS_DIR} --check || :

check-isort:
	$(ISORT) ${SOURCE_DIR} --check || :
	$(ISORT) ${TESTS_DIR} --check || :

check-pydocstyle:
	$(PYDOCSTYLE) ${SOURCE_DIR} || :

check-mypy:
	$(MYPY) ${SOURCE_DIR} || :

check-flake8:
	$(FLAKE8) ${SOURCE_DIR} || :
	$(FLAKE8) ${TESTS_DIR} || :

check: check-black check-isort check-mypy check-flake8 check-pydocstyle

pre-commit:
	$(PRECOMMIT) run --all-files

format-black:
	$(BLACK) ${SOURCE_DIR}
	$(BLACK) ${TESTS_DIR}
	$(BLACK) ${EXAMPLES_DIR}

format-isort:
	$(ISORT) ${SOURCE_DIR}
	$(ISORT) ${TESTS_DIR}

format: format-black format-isort

clean-doc:
	$(MAKE) -C ${DOCDIR} clean

clean-build:
	$(PYTHON) setup.py clean
	rm -rf ${DIST}

# Clean up any builds in ./dist as well as doc
clean: clean-doc clean-build

# Build a distribution in ./dist
build:
	$(PYTHON) setup.py bdist

docs:
	$(MAKE) -C ${DOCDIR} doc
	@echo
	@echo "View docs at:"
	@echo ${INDEX_HTML}

examples:
	$(MAKE) -C ${DOCDIR} examples
	@echo
	@echo "View docs at:"
	@echo ${INDEX_HTML}

# Publish to testpypi
# Will echo the commands to actually publish to be run to publish to actual PyPi
# This is done to prevent accidental publishing but provide the same conveniences
publish: clean-build build
	$(PIP) install twine
	$(PYTHON) -m twine upload --repository testpypi ${DIST}/*
	@echo "Uploaded to testpypi so the distribution can be tested"
	@echo
	@echo "Test with the following lines:"
	@echo "pip install --index-url https://test.pypi.org/simple/ ${NAME}"
	@echo "make test"
	@echo
	@echo "Once you have decided it works, publish to actual pypi with"
	@echo "python -m twine upload dist/*"

test:
	$(PYTEST) ${TESTS_DIR}
