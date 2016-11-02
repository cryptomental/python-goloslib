.PHONY: clean-pyc clean-build docs

TAG := $(shell git describe master --abbrev=0)
TAGGOLOS := $(shell git describe master --abbrev=0 | tr "." "-")

# 
clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	rm -fr __pycache__/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	flake8 golosapi/ golosbase/

test:
	python3 setup.py test

build:
	python3 setup.py build

install: build
	python3 setup.py install

install-user: build
	python3 setup.py install --user

git:
	git push --all
	git push --tags

check:
	python3 setup.py check

dist:
	python3 setup.py sdist upload -r pypi
	python3 setup.py bdist --format=zip upload
	python3 setup.py bdist_wheel upload

release: clean check dist golos-changelog git

golos-changelog:
	git show -s --pretty=format: $(TAG) | tail -n +4 | piston post --file "-" --author xeroc --permlink "python-goloslib-changelog-$(TAGGOLOS)" --category golos --title "[Changelog] python-golos $(TAG)" --tags python-goloslib changelog
