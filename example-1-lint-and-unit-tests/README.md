# Example 1 - Lint and Unit Tests 

## TL;DR:

Example 1 is a simple workflow which runs linting and unit tests for a Python project.

## Code

Within `src/` there is a file [`paddle.py`](./src/paddle.py) which contains a very simple function which returns `'pong'`.

Within `tests/` there is a file [`test_paddle.py`](./tests/test_paddle.py) which asserts that the function returns `'pong'`.

## Workflow

Within [`.github/workflows/example-1-lint-and-unit-tests.yaml`](../.github/workflows/example-1-lint-and-unit-tests.yaml), we're defining two `jobs`. Both jobs carry out the same steps first:

* Checkout the code
* Install Python
* Install Poetry
* Install Dependencies

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
