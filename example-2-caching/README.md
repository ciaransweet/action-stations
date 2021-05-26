# Example 1 - Caching

## TL;DR:

Example 2 is a duplicate of Example 1, but this time we make use of [`actions/cache@v2`](https://github.com/actions/cache) to cache dependencies to save build time on subsequent workflow runs. The code under test is different to highlight that we're using a different set of dependencies.

## Code

Within `src/` there is a file [`get_datetime.py`](./src/get_datetime.py) which contains a very simple function which returns `datetime.now()`.

Within `tests/` there is a file [`test_get_datetime.py`](./tests/test_get_datetime.py) which uses [`freezegun`](https://github.com/spulec/freezegun) to 'freeze' the time within the test and asserts that `get_datetime` returns the correct datetime.

## Workflow

Within [`.github/workflows/example-2-caching.yaml`](../.github/workflows/example-2-caching.yaml), we're defining two `jobs`. Both jobs carry out the same steps first:

* Checkout the code
* Install Python
* Install Poetry
* Setup Cache
* Install Dependencies - If no cache present

Then, the jobs either run `lint` or `unit-tests`.

This workflow **only** runs when either a commit is pushed to the `main` branch, or when a pull request is raised against the `main` branch.

# Development

To get setup, run:

```bash
$ make install # Installs the dependencies in `pyproject.toml`, sets up a Poetry Virtual Environment, and echoes its location for use in IDEs
```

To lint the code in `src/` and `tests/`, run:

```bash
$ make lint # Runs flake8, isort, and black in check only mode and outputs any linting issues
```

To format the code in `src/` and `tests/`, run:

```bash
$ make format # Runs isort and black, formatting your code
```

To run the unit tests, run:

```bash
$ make unit-tests # Runs the unit test suite in `tests/`
```
