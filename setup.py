#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:54:21 2020

@author: advait_t
"""

import setuptools

with open("readme.txt", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pneumonia_x-ray", # Replace with your own username
    version="0.0.1",
    author="Advait Thergaonkar, Jay Prajapati",
    author_email="advait.thergaonkar@gmail.com , jayprajapati1141@gmail.com",
    description="A package made to test X-Ray images to determine pneumonia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
