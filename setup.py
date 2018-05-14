#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name="Pycurl_Phabricator",
    description="Pycurl based Phabricator API library",
    long_description_content_type='text/markdown',
    long_description=open('README.md', encoding='utf8').read(),
    keywords="phabricator python pycurl",

    url="https://github.com/Cuile/pycurl_Phabricator",
    packages=['Conduit'],
    version="0.2.2",
    install_requires=['pycurl == 7.43.0.1', 'certifi == 2018.1.18', 'sequence2hash'],

    author="Cuile",
    author_email="i@cuile.com",
)
