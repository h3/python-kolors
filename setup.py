# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='kolors',
    version='0.0.1',
    description='Simple and lightweight shell color output function.',
    long_description=(read('README.md')),
    author='Maxime Haineault',
    author_email='haineault@gmail.com',
    license='MIT',
    url='https://github.com/h3/python-kolors',
    packages=find_packages(),
    include_package_data=True,
    package_data={'kolors': [
        'README.rst',
        'CHANGELOG',
        ]},
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
