#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django-humans-txt
# setup.py

from setuptools import (
    setup,
    find_packages,
)


# metadata
VERSION = (0, 0, 0)
__version__ = ".".join(map(str, VERSION))

setup(
    name="django-humans-txt",
    version=__version__,
    packages=find_packages(),
    install_requires=["Django", ],
    author="Alexei Andrushievich",
    author_email="vint21h@vint21h.pp.ua",
    description="Handle humans.txt",
    license="GPLv3 or later",
    url="https://github.com/vint21h/django-humans-txt/",
    download_url="https://github.com/vint21h/django-humans-txt/archive/{version}.tar.gz".format(version=__version__),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Environment :: Plugins",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
    ]
)
