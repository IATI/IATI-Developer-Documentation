Notes about IATI Python Code
============================

Python2 vs Python3
------------------

Currently all IATI code is Python 2, and in general isn't Python 3. However, we have started some Python 3 features (e.g. the Python 3 print statement) in new code to make a future transition easier.

Common Dependencies
-------------------

A lot of our software has dependencies in common:

* lxml, a fast XML toolkit that uses C libraries
* Flask as the web framework
* Jinja as the templating engine (including for use with Sphinx)
* py.test - a no-boilerplate testing framework (although some code also uses nosetest and plain unit test)

Pinned Dependencies
-------------------

We pin all our dependencies (including dependencies of dependencies) to an exact version in requirements.txt. This makes deployment more deterministic and reproducible. It also means that we can use requires.io to track out of date dependencies.

virtualenv
----------

In order to install multiple version of the same dependency for different projects, we use `virtualenv <https://virtualenv.pypa.io/en/latest/>`__.

Python Packages
---------------

Currently most of our Python code is standalone scripts rather than python packages (ie. with a setup.py and installable with pip). The two current packages are IATI-Rulesets and iati-datastore, but versioning information in these is not maintained (as the preferred installation method is via GitHub).
