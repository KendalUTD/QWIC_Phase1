#!/usr/bin/env python

from setuptools import setup

setup(name="cyberminer",
    version="0.1",
    description="A simple web search engine based on KWIC.",
    author="Abdul Ghulam, Ch Divyesh venkata rama kumar, Hunter Sullivan, Kendal Wiggins, Mohammad Rafieian",
    packages=["cyberminer", "kwic"],
    entry_points={
        "console_scripts": [
            "cyberminer = cyberminer:main",
        ],
    }
)