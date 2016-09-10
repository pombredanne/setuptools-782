#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import os
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


setup(
    name='setuptools-bug-good',
    version='1.0.0',
    license='Apache-2.0',
    description='https://github.com/pypa/setuptools/issues/782',
    long_description='https://github.com/pypa/setuptools/issues/782',
    url='https://github.com/pombredanne/setuptools-782',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=['Development Status :: 4 - Beta',],
    install_requires=['unicodecsv',],
    extras_require={
        ':platform_system == "Windows"': ['lxml == 3.6.0'],
        ':platform_system == "Linux"': ['lxml == 3.6.4'],
        ':platform_system == "Darwin"': ['lxml == 3.6.4'],
    },
    entry_points={'console_scripts': ['bug = bug:run'],
    }
)
