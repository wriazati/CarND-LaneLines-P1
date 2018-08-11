#! /usr/bin/env python

from os.path import dirname, realpath, join
from setuptools import setup, find_packages


####
# Basic metadata.
####

project_name = 'CarND-LaneLines-P1'
package_name = project_name.replace('-', '_')
repo_name    = project_name
description  = 'CarND-LaneLines-P1'
url          = 'https://github.com/wriazati/' + repo_name
author       = 'wriazati'
author_email = author + '@yahoo.com'


####
# Requirements.
####

reqs = [
    # Our packages.
    'ipython',
	'numpy',
	'matplotlib',
    'scipy',
    'jupyter',
    'pillow',
]

extras = {
    'test' : [
        'pytest'
    ],
    'dev' : [
    ],
}


####
# Packages and scripts.
####

entry_points = {
    'console_scripts': [
        'run = mnist_cnn:main',
    ],
}


####
# Import __version__.
####

project_dir = dirname(realpath(__file__))


####
# Install.
####

setup(
    name             = project_name,
    version          = "1.0",
    author           = author,
    author_email     = author_email,
    url              = url,
    description      = description,
    zip_safe         = False,
    install_requires = reqs,
    tests_require    = extras['test'],
    extras_require   = extras,
    entry_points     = entry_points,
)
