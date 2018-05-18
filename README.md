# OmMongo
[![Documentation Status](https://readthedocs.org/projects/ommongo/badge/?version=latest)](http://ommongo.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/bapakode/OmMongo.svg?branch=master)](https://travis-ci.org/bapakode/OmMongo)
[![Coverage Status](https://coveralls.io/repos/github/bapakode/OmMongo/badge.svg?branch=master)](https://coveralls.io/github/bapakode/OmMongo?branch=master)
[![Python Version Support](https://img.shields.io/badge/python-2.7%20--%203.5-blue.svg)](https://www.python.org/)

OmMongo is Object Relational Mapping for MongoDB, this project is forked from MongoAlchemy project.

--------
### Installation

Install using Python PIP
	
	sudo pip install OmMongo

or download this repository and run setup.py

	sudo python setup.py install

### Documentation

The documentation can be found here [https://ommongo.readthedocs.io/en/latest/index.html](https://ommongo.readthedocs.io/en/latest/index.html "OmMongo Documentation")

### Test

	sudo pip install -r requirements.testing.txt

Test setup.py

	coverage run --source=ommongo setup.py test

Nose Tests

	nosetests --cover-tests --cover-erase --with-coverage --cover-package ommongo
