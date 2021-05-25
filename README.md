# 🚨 Action Stations! 🚨 ![CI Build Status](https://github.com/ciaranevans/action-stations/actions/workflows/ci.yaml/badge.svg)

Welcome to `action-stations` - A repository where I'll try to demo a few examples of GitHub Actions and how to use them 🎉

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
