# Cyberminer

This python project consists of two modules:

* __kwic__ - a simple implementation for a Key Word In Context system. 
* __cyberminer__ - a flask application which provides a frontend for a simple web search engine. This web search engine makes use of _kwic_ to query search results stored in a local database. 

## Prerequisites

* Python 3

## Getting started

```
$ git clone git@github.com:KendalUTD/QWIC_Phase1.git
$ cd QWIC_Phase1
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python setup.py develop
$ cyberminer
```
