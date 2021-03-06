#!/usr/bin/env python

from setuptools import setup

setup(
    name='salt-cloud-provider-vcloud',
    version='0.1.1-alpha',
    url='http://github.com/ministryofjustice/',
    license='TBD',
    author='',
    author_email='',
    description='',
    long_description=__doc__,
    packages=['salt.cloud.clouds.vcloud_support', 'salt.cloud.clouds'],
    namespace_packages=['salt.cloud.clouds', 'salt.cloud', 'salt'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'pyyaml',
        'jinja2',
        'lxml',
        'apache-libcloud>=0.14.1',
        'salt>=2014.1.0',
    ],
    classifiers=[
    ],
)
