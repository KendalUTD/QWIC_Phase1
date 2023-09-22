#!/usr/bin/env python

from setuptools import setup

setup(name="kwic",
    version="0.1",
    description="A prototype Key Word In Context (KWIC) application.",
    author="Abdul Ghulam, Ch Divyesh venkata rama kumar, Hunter Sullivan, Kendal Wiggins, Mohammad Rafieian",
    packages=["kwic"],
    entry_points={
        "console_scripts": [
            "kwic = kwic:main",
        ],
    }
)