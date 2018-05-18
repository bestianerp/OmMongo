#!/usr/bin/env python

import setuptools
from distutils.core import setup

VERSION = '1.1.2'
DESCRIPTION = 'Document-Object Mapper/Toolkit for Mongo Databases'
LONG_DESCRIPTION = open('README.md', 'r').read()

setup(
    name='OmMongo',
    version=VERSION,
    description=DESCRIPTION,
	long_description=LONG_DESCRIPTION,
	long_description_content_type='text/markdown',
    author='Bapakode Open Source',
    license='MIT',
    author_email='opensource@bapakode.com',
    url='https://github.com/bapakode/ommongo',
    packages=['ommongo', 'ommongo.fields'],
    install_requires=['pymongo'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)