#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import platform
import re
import warnings
import pprint
pp = pprint.PrettyPrinter(indent=4)


# Don't force people to install setuptools unless
# we have to.
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from setuptools.command import install_lib
from scarlett_os.const import (__version__, PROJECT_PACKAGE_NAME,
                               PROJECT_LICENSE, PROJECT_URL,
                               PROJECT_EMAIL, PROJECT_DESCRIPTION,
                               PROJECT_CLASSIFIERS, GITHUB_URL,
                               PROJECT_AUTHOR)

HERE = os.path.abspath(os.path.dirname(__file__))
DOWNLOAD_URL = ('{}/archive/'
                '{}.zip'.format(GITHUB_URL, __version__))

# PACKAGES = find_packages(exclude=['tests', 'tests.*'])
PACKAGE_NAME = PROJECT_PACKAGE_NAME

print('Current Python Version, B: {}'.format(sys.version_info))

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

static = {}

for root, dirs, files in os.walk('static'):
    for filename in files:
        filepath = os.path.join(root, filename)

        if root not in static:
            static[root] = []

        static[root].append(filepath)

# Might use this later
try:
    here = os.path.abspath(os.path.dirname(__file__))
except:
    pass


def read_requirements(filename):
    content = open(os.path.join(here, filename)).read()
    requirements = map(lambda r: r.strip(), content.splitlines())
    return requirements


requirements = [
    'Click>=6.0',
    'click-plugins',
    'pydbus>=0.5.0',
    'colorlog>=2.7',
    'jinja2>=2.8',
    'typing>=3,<4',
    'psutil>=4.3.0',
    'six',
    'voluptuous==0.9.2',
    'Fabric3==1.12.post1',
    'PyYAML>=3.0'
]


test_requirements = [
    'pytest>=3.0',
    'pytest-timeout>=1.0.0',
    'pytest-catchlog>=1.2.2',
    'pytest-cov>=2.3.1',
    'pip>=7.0',
    'bumpversion>=0.5.3',
    'wheel>=0.29.0',
    'watchdog>=0.8.3',
    'flake8>=2.6.2',
    'flake8-docstrings>=0.2.8',
    'coverage>=4.1',
    'Sphinx>=1.4.5',
    'cryptography==1.5.2',
    'PyYAML>=3.11',
    'pydocstyle>=1.0.0',
    'mypy-lang>=0.4',
    'pylint>=1.5.6',
    'coveralls>=1.1',
    'ipython>=5.1.0',
    'gnureadline>=6.3.0',
    'requests_mock>=1.0',
    'mock-open>=1.3.1',
    'mock',
    'pytest-benchmark[histogram]>=3.0.0rc1',
    'python-dbusmock',
    'freezegun'
]


# Pytest
class PyTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests', '--ignore', 'tests/sandbox', '--verbose']
        # self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


# check_python_version()


setup(
    name=PROJECT_PACKAGE_NAME,
    version=__version__,
    description=PROJECT_DESCRIPTION,
    long_description=readme + '\n\n' + history,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,
    packages=[
        'scarlett_os',
    ],
    package_dir={'scarlett_os':
                 'scarlett_os'},
    #              ,
    # entry_points={
    #     'console_scripts': [
    #         'ss = scarlett_os.__main__:main'
    #     ]
    # },
    # entry_points={
    #     'console_scripts': [
    #         'scarlett_os=scarlett_os.cli:main'
    #     ]
    # },
    # source: mapbox-cli-py
    entry_points="""
    [console_scripts]
    scarlett_os=scarlett_os.scripts.cli:main_group

    [scarlett_os.scarlett_os_commands]
    config=scarlett_os.scripts.config:config
    """,
    # geocoding=mapboxcli.scripts.geocoding:geocoding
    # directions=mapboxcli.scripts.directions:directions
    # distance=mapboxcli.scripts.distance:distance
    # mapmatching=mapboxcli.scripts.mapmatching:match
    # upload=mapboxcli.scripts.uploads:upload
    # staticmap=mapboxcli.scripts.static:staticmap
    # surface=mapboxcli.scripts.surface:surface
    # dataset=mapboxcli.scripts.datasets:datasets
    extras_require={
        'test': test_requirements,
    },
    include_package_data=True,
    install_requires=requirements,
    license=PROJECT_LICENSE,
    zip_safe=False,
    keywords='scarlett_os',
    classifiers=PROJECT_CLASSIFIERS,
    test_suite='tests',
    tests_require=test_requirements,
    cmdclass={'test': PyTest}
)
