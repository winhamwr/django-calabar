#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages, Command

import django_calabar

long_description = codecs.open("README.rst", "r", "utf-8").read()

setup(
    name='django_calabar',
    version=django_calabar.__version__,
    description=django_calabar.__doc__,
    author=django_calabar.__author__,
    author_email=django_calabar.__contact__,
    url=django_calabar.__homepage__,
    platforms=["any"],
    license="BSD",
    packages=find_packages(),
    scripts=[],
    zip_safe=False,
    install_requires=[],
    extra_requires={},
    cmdclass = {},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "Programming Language :: Python",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Topic :: Internet",
        "Topic :: System :: Networking",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=long_description,
)