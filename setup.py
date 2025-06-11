#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

version = "0.0.4"

setuptools.setup(
    name="plugin-cli",
    version=version,
    author="SongZhao",
    author_email="zhaosonggo@gmail.com",
    description="Rapidly Build a Plugin-Based CLI Tool Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="git@github.com:ZhaoSongGOO/tools-box.git",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": ["tools-box=cli.app:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
