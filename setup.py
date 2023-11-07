#!/usr/bin/env python

from setuptools import setup

setup(name="kwic",
    version="0.1",
    description="A simple search engine based on KWIC.",
    author="Abdul Ghulam, Ch Divyesh venkata rama kumar, Hunter Sullivan, Kendal Wiggins, Mohammad Rafieian",
    packages=["engine", "kwic"],
    entry_points={
        "console_scripts": [
            "thunder = engine:main",
        ],
    }
)