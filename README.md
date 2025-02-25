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

To avoid manually changing the version number in multiple places (e.g. `setup.py`, `pyproject.toml`, and git tags), one can use `setuptools_scm` to automatically manage the versioning from git records. This way, the version number is derived from the latest git tag. In case there is no tag, it will use branch and the latest commit hash. The essential bits in the `pyproject.toml` file are:

```toml
[build-system]
requires = ["setuptools>=64", "setuptools-scm>=8"]
build-backend = "setuptools.build_meta"

[project]
dynamic = ["version"]


[tool.setuptools_scm]
```

To check the version, you can run:

```bash
$ python -m setuptools_scm
0.1.dev1+g5080c63
$ git tag 0.1.0
$ python -m setuptools_scm
0.1.0
```

Check [setuptools dynamic metadata](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#static-vs-dynamic-metadata) and
[setuptools_scm](https://github.com/pypa/setuptools-scm) for more information.

## Testing

I use `unittest` for testing. For each module you would like to test, create a corresponding test file in the `tests` directory. The test files should be named `test_<module_name>.py`. 

To run the tests, you can use the following command:

```bash
$ python -m unittest discover tests
```

## References

- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
