Python Library for Golos
========================

Python 3 library for Golos!

**Stable**

[![docs master](https://readthedocs.io/projects/python-steem/badge/?version=latest)](http://python-steem.readthedocs.io/en/latest/)
[![Travis master](https://travis-ci.org/xeroc/python-steem.png?branch=master)](https://travis-ci.org/xeroc/python-steem)
[![codecov](https://codecov.io/gh/xeroc/python-steem/branch/master/graph/badge.svg)](https://codecov.io/gh/xeroc/python-steem)


[![PyPI](https://img.shields.io/pypi/dm/steem.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/dw/steem.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/dd/steem.svg?maxAge=2592000)]()

**Develop**

[![docs develop](https://readthedocs.io/projects/python-steem/badge/?version=develop)](http://python-steem.readthedocs.io/en/develop/)
[![Travis develop](https://travis-ci.org/xeroc/python-steem.png?branch=develop)](https://travis-ci.org/xeroc/python-steem)
[![codecov develop](https://codecov.io/gh/xeroc/python-steem/branch/develop/graph/badge.svg)](https://codecov.io/gh/xeroc/python-steem)

Installation
------------

Install with `pip`:

    $ sudo apt-get install libffi-dev libssl-dev python-dev
    $ pip3 install golos

Manual installation:

    $ git clone https://github.com/GolosChain/python-goloslib
    $ cd python-goloslib
    $ python3 setup.py install --user

Upgrade
-------

    $ pip install --user --upgrade

Additional dependencies
-----------------------

`golosapi.golosasyncclient`:
 * `asyncio==3.4.3`
 * `pyyaml==3.11`

Documentation
-------------

Thanks to readthedocs.io, the documentation can be viewed
[online](http://python-goloslib.readthedocs.io/en/latest/)

Documentation is written with the help of sphinx and can be compile to
html with:

    cd docs
    make html
