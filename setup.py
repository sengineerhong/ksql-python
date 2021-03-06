#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Setup module """
import os
import re

from setuptools import setup
from pip.req import parse_requirements

# Get version from __init__.py file
VERSION = "0.3.0.2.22"

here = os.path.dirname(__file__)

# Get long description
README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

reqs = ['requests',
        'six',
        'urllib3']

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="ksql",
    version=VERSION,
    description="A Python wrapper for the KSql REST API",
    long_description=README,
    author="Bryan Yang @ Vpon",
    author_email="kenshin200528@gmail.com",
    url="https://github.com/bryanyang0528/ksql-python",
    license="MIT License",
    packages=[
        "ksql"
    ],
    include_package_data=True,
    platforms=['any'],
    install_requires=reqs,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
