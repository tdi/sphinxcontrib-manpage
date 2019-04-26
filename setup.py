#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
        from setuptools import setup, find_packages
except ImportError:
        from distutils.core import setup, find_packages

# tested only with it, if you tested with older version and it worked, pleas
# let me know
requires = ['Sphinx>=0.9'] 

setup(

    name='sphinxcontrib-manpage',
    version='0.6',
    url='https://github.com/tdi/sphinxcontrib-manpage',
    author='Dariusz Dwornikowski',
    author_email='dariusz.dwornikowski@cs.put.poznan.pl',
    description='Sphinx linux manpage extension',
    long_description=open('README.rst').read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
    ],
    platforms='any',
    license = "Apache Common 2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
