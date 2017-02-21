# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from setuptools import setup, find_packages

from smartship import __version__


description = "Posti SmartShip API"


def get_long_description():
    return open(os.path.join(os.path.dirname(__file__), "docs", "introduction.rst")).read()


setup(
    name='smartship',
    version=__version__,
    description=description,
    # long_description=get_long_description(),
    author='Anders Innovations',
    author_email='support@anders.fi',
    maintainer='Anders Innovations',
    maintainer_email='support@anders.fi',
    url='https://github.com/andersinno/smartship',
    download_url='https://github.com/andersinno/smartship/releases',
    packages=find_packages(
        exclude=[
            "tests",
        ],
    ),
    license="?????",
    install_requires=[
        "attrs>=16.2.0,<17",
        "jsonschema>=2.0,<3",
        "requests>=2.11.1,<3",
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='smartship posti',
)
