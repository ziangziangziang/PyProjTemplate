# Tips on creating a Python package

- [Tips on creating a Python package](#tips-on-creating-a-python-package)
  - [Directory structure](#directory-structure)
  - [Installing the package from git repo](#installing-the-package-from-git-repo)
  - [Single source versioning with `git tag`](#single-source-versioning-with-git-tag)
  - [Testing](#testing)
    - [Test env setup with `tox`](#test-env-setup-with-tox)
    - [Unit testing](#unit-testing)
    - [Integration testing](#integration-testing)
    - [TODO](#todo)
  - [References](#references)


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
├── examples
│   ├── example1.py
│   └── example2.py
├── localtest # excluded in .gitignore
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
└── tests
    ├── __init__.py
    ├── test_module1.py
    └── test_module2.py
```

The above is my directory structure. The `src` directory contains the package code, and the `tests` directory contains the test code. The `localtest` directory is for local testing and should not be ignored in the `.gitignore` file. The `__init__.py` files are used to mark directories as Python packages.

## Installing the package from git repo

It's easy to install a python package if the package was a git repository without cloning the repo and installing it manually. For example, to install this package, do

```bash
pip install 'git+ssh://git@github.com/ziangziangziang/PyProjTemplate.git' # for SSH url
pip install 'git+https://github.com/ziangziangziang/PyProjTemplate.git' # for HTTPS url

```

## Single source versioning with `git tag`

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
$ git tag v0.1.0 # "v" prefix is preferred
$ python -m setuptools_scm
0.1.0
```

Check [setuptools dynamic metadata](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#static-vs-dynamic-metadata) and
[setuptools_scm](https://github.com/pypa/setuptools-scm) for more information.

## Testing

Testing is to ensure the package works as expected. Besides "unit testing" and "integration testing", I also have a "local testing" in the directory structure. 
The "local testing" is for testing the package locally using local data/environment. It will be excluded in the git workspace.

For testing, I use `unittest` for unit testing and `pytest` for integration testing. `tox` is used for creating and managing virtual environments for testing.

The testing dependencies are specified in the `pyproject.toml` file as the optional dependencies. They will only be installed when you run `pip install ".[test]"`.


### Test env setup with `tox`

Since release `3.24.5`, `tox` can take native configuraion from `pyproject.toml`. In our project, we use this feature to create tox envirnoments and run tests. The configuration was specified in the `tool.tox` section in the `pyproject.toml` file. 


### Unit testing
I use `unittest` for testing. For each module you would like to test, create a corresponding test file in the `tests` directory. The test files should be named `test_<module_name>.py`. 

To run the tests, you can use the following command:

```bash
$ python -m unittest discover tests
```

### Integration testing

Integration testing is to test the package as a whole. The integration tests are usually written in the `tests` directory. The integration tests can be run using the following command:


### TODO

- [x] Add multi-environment testing with `tox`.
- [x] Implement `tox` testing in `project.toml` file when the native support was ready. The development was on the way, see[this issue](https://github.com/tox-dev/tox/issues/999)

## References

- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
