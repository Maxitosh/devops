# Best practices for Python and Markdown

## Python

### Web frameworks

* [Gunicorn](https://github.com/benoitc/gunicorn/) - is a Python WSGI HTTP Server for UNIX.
* [Django](https://www.djangoproject.com/) - is a high-level Python Web framework that encourages rapid development and
  clean, pragmatic design.
* [web2py](https://www.web2py.com/) - free open source full-stack framework for rapid development of fast, scalable,
  secure and portable database-driven web-based applications.
* [Flask](https://palletsprojects.com/p/flask/) - is a lightweight WSGI web application framework. It is designed to
  make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple
  wrapper around Werkzeug and Jinja.
* [**FastAPI**](https://fastapi.tiangolo.com/) is a modern, fast (high-performance), web framework for building APIs
  with Python 3.6+ based on standard Python type hints.

### Linters

* [**Pylint**](http://pylint.pycqa.org/en/latest/) - checks for errors, tries to enforce a coding standard
* [PyFlakes](https://github.com/PyCQA/pyflakes) - analyzes programs and detects various errors
* [pycodestyle](https://github.com/PyCQA/pycodestyle) - checks against style conventions in PEP 8
* [pydocstyle](https://github.com/PyCQA/pydocstyle) - checks compliance with Python docstring conventions
* [Bandit](https://bandit.readthedocs.io/en/latest/) - analyzes code to find common security issues
* [MyPy](https://mypy.readthedocs.io/en/stable/) - checks for optionally-enforced static types

### Formatters and analyzers

* [**Black**](https://github.com/psf/black) - formats Python code without compromise
* [Radon](https://radon.readthedocs.io/en/latest/) - analyzes code for various metrics (lines of code, complexity, and
  so on)
* [Isort](https://github.com/PyCQA/isort) - formats imports by sorting alphabetically and separating into sections

## Markdown

* [**Markdown Lint**](https://github.com/DavidAnson/markdownlint) - node.js markdown linter that is easy to install and
  easy to customize.
* [mdspell](https://www.npmjs.com/package/markdown-spellcheck) - is a tool specifically for spelling checking markdown
  documents.
* [alex](https://alexjs.com/) - catches insensitive and inconsiderate writing, it supports markdown files.
* [write-good](https://github.com/btford/write-good) - the tool’s focus is on improving the clarity of writing.
* [textlint](https://textlint.github.io/) - is a pluggable linting tool that supports markdown, plain text, and HTML.
* [proselint](http://proselint.com/) - goes deep on writing clarity improvements.

## Testing

* [**pytest**](https://docs.pytest.org/en/6.2.x/) - The pytest framework makes it easy to write small tests, yet scales
  to support complex functional testing for applications and libraries.
* [unittest](https://docs.python.org/3/library/unittest.html) - The unittest unit testing framework was originally
  inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test
  automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of
  the tests from the reporting framework.

## Best practices for Testing

* A testing unit should focus on one tiny bit of functionality and prove it correct.
* If one single test needs more than a few milliseconds to run, development will
  be slowed down or the tests will not be run as often as is desirable. In some cases, tests can’t be fast because they
  need a complex data structure to work on, and this data structure must be loaded every time the test runs. Keep these
  heavier tests in a separate test suite that is run by some scheduled task, and run all other tests as often as needed.
* It is a good idea to implement a hook that runs all tests before pushing code to a shared repository.
* Always run the full test suite before a coding session, and run it again after.
* Tests Shouldn’t Duplicate Implementation Logic.
* Tests Should Be Readable.
