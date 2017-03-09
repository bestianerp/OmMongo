#!/usr/bin/env python

import setuptools
from distutils.core import setup

VERSION = '1.0'
DESCRIPTION = 'Document-Object Mapper/Toolkit for Mongo Databases'

setup(
    name='OmMongo',
    version=VERSION,
    description=DESCRIPTION,
    author='Bapakode Open Source',
    license='MIT',
    author_email='opensource@bapakode.org',
    url='http://bapakode.org/ommongo',
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