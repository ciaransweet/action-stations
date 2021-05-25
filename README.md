# 🚨 Action Stations! 🚨 ![CI Build Status](https://github.com/ciaranevans/action-stations/actions/workflows/ci.yaml/badge.svg)

Welcome to `action-stations` - A repository where I'll try to demo a few examples of GitHub Actions and how to use them 🎉

# Development

## Requirements

* [Python 3.8.*](https://www.python.org/downloads/) (I recommend using [pyenv](https://github.com/pyenv/pyenv) to handle Python versions)
* [Poetry](https://github.com/python-poetry/poetry)

If you're developing on MacOS, the above can be installed using [homebrew](https://brew.sh/)

If you're developing on Windows, I'd recommend using either [Git BASH](https://gitforwindows.org/) or [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

_I provide a [`Makefile`](./Makefile) to try and abstract away some of the commonly used commands, so you may want to get `make` also_

## Getting Started

Once you've gotten setup with the [Requirements](#requirements), you can setup your Python environment by running:

```bash
$ poetry install # Installs the dependencies in `pyproject.toml` and sets up a Poetry Virtual Environment
$ poetry env info -p # Outputs the location of your Virtual Environment (You can use this to get completions in your IDE)

# Of if you're using the Makefile:

$ make install # Installs the dependencies in `pyproject.toml`, sets up a Poetry Virtual Environment, and echoes its location
```

# Makefile

A `Makefile` is provided to abstract away common commands:

```bash
---

$ make install # Installs the dependencies in `pyproject.toml`, sets up a Poetry Virtual Environment, and echoes its location for use in IDEs

---

$ make lint # Runs flake8, isort, and black in check only mode and outputs any linting issues

---

$ make format # Runs isort and black, formatting your code

---

$ make unit-tests # Runs the unit test suite in `tests/`

---
```
