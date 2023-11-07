#!/usr/bin/env python

from setuptools import find_packages, setup

print(f"Installing {find_packages()}")
setup(
    name="simple-ml",
    version="0.1.0",
    description="Simple ML",
    author="Antreas Antoniou",
    author_email="iam@antreas.io",
    packages=find_packages(),
)
