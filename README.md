# 🚨 Action Stations! 🚨

Welcome to `action-stations` - A repository where I'll try to demo a few examples of GitHub Actions and how to use them 🎉

# Examples

[![Example-1](https://github.com/ciaranevans/action-stations/actions/workflows/example-1-lint-and-unit-tests.yaml/badge.svg)](https://github.com/ciaranevans/action-stations/actions/workflows/example-1-lint-and-unit-tests.yaml)
[![README](https://img.shields.io/static/v1?label=README&message=CLICK-HERE&logo=markdown&color=green)](./example-1-lint-and-unit-tests/README.md)

[![Example-2](https://github.com/ciaranevans/action-stations/actions/workflows/example-2-caching.yaml/badge.svg)](https://github.com/ciaranevans/action-stations/actions/workflows/example-2-caching.yaml)
[![README](https://img.shields.io/static/v1?label=README&message=CLICK-HERE&logo=markdown&color=green)](./example-2-caching/README.md)

[![Example-3](https://github.com/ciaranevans/action-stations/actions/workflows/example-3-manual-invocation.yaml/badge.svg)](https://github.com/ciaranevans/action-stations/actions/workflows/example-3-manual-invocation.yaml)
[![README](https://img.shields.io/static/v1?label=README&message=CLICK-HERE&logo=markdown&color=green)](./example-3-manual-invocation/README.md)

[![Example-4](https://github.com/ciaranevans/action-stations/actions/workflows/example-4-manual-invocation-with-parameters.yaml/badge.svg)](https://github.com/ciaranevans/action-stations/actions/workflows/example-4-manual-invocation-with-parameters.yaml)
[![README](https://img.shields.io/static/v1?label=README&message=CLICK-HERE&logo=markdown&color=green)](./example-4-manual-invocation-with-parameters/README.md)

[![Example-5](https://github.com/ciaranevans/action-stations/actions/workflows/example-5-cdk-with-environments.yaml/badge.svg)](https://github.com/ciaranevans/action-stations/actions/workflows/example-5-cdk-with-environments.yaml)
[![README](https://img.shields.io/static/v1?label=README&message=CLICK-HERE&logo=markdown&color=green)](./example-5-cdk-with-environments/README.md)

[![Example-6](https://github.com/ciaranevans/action-stations/actions/workflows/example-6-actions-action.yaml/badge.svg)](https://github.com/ciaranevans/action-stations/actions/workflows/example-6-actions-action.yaml)
[![README](https://img.shields.io/static/v1?label=README&message=CLICK-HERE&logo=markdown&color=green)](./example-6-actions-action/README.md)

# Development

## Requirements

### All Examples
* [Python 3.8.*](https://www.python.org/downloads/) (I recommend using [pyenv](https://github.com/pyenv/pyenv) to handle Python versions)
* [Poetry](https://github.com/python-poetry/poetry)

### CDK Examples
* [Node 14](https://nodejs.org/en/) (I recommend using NVM [Node Version Manager](https://github.com/nvm-sh/nvm))
* [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) - There is a `package.json` in the cdk examples, it's recommended to run `npm install` in the examples directories and make use of `npx <command>` rather than globally installing AWS CDK
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

If you're developing on MacOS, the above can be installed using [homebrew](https://brew.sh/)

If you're developing on Windows, I'd recommend using either [Git BASH](https://gitforwindows.org/) or [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

_I provide a [`Makefile`](./Makefile) to try and abstract away some of the commonly used commands, so you may want to get `make` also_
