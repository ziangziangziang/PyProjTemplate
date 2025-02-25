[TOC]

# Tips on creating a Python package

## Directory structure

```bash
.
├── .gitignore
├── README.md
├── setup.py
├── pyproject.toml
├── src
│   └── my_package
│       ├── __init__.py
│       ├── module1.py
│       └── module2.py
├── localtest
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
└── tests
    ├── __init__.py
    ├── test_module1.py
    └── test_module2.py
```

The above is my directory structure. The `src` directory contains the package code, and the `tests` directory contains the test code. The `localtest` directory is for local testing and should not be ignored in the `.gitignore` file. The `__init__.py` files are used to mark directories as Python packages.

## Single source versioning

To avoid manually change the version number in multiple places (e.g. `setup.py`, `pyproject.toml`, and git tags),which

[setuptools dynamic metadata](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#static-vs-dynamic-metadata)
