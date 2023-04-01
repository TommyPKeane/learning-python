# Python Standard Library (PSL) Examples

This directory contains custom examples demonstrating the features and functionality in the Python Standard Library (PSL) using the latest stable release of Python.

<!-- MarkdownTOC -->

- [Setup](#setup)
- [Examples](#examples)
- [References](#references)
- [License](#license)

<!-- /MarkdownTOC -->

<a id="setup"></a>
## Setup

Developer setup for this repo is based-on [`direnv`](https://direnv.net/) and [`pyenv`](https://github.com/pyenv/pyenv), instead of using a Dockerized environment. This can allow for really easy local testing and development in Linux or macOS (with minor edits, or use of the WSL, to be used in Windows 10/11).

This was all tested and verified with macOS by installing `direnv` and `pyenv` with [`brew`](https://brew.sh/):

1. `brew install direnv`
1. `brew install pyenv`

Once you have these tools installed and configured properly for your system (a personal example can be followed with more details on my own GitHub Account for my preferred [`bash` Configuration](https://github.com/TommyPKeane/example-bash-configuration)), you should then be able to run the following commands to setup this repo for the first time for development:

1. `pyenv install` (Optional; only needed, once, if you don't have the `.python-version` version already installed)
1. `direnv allow`
1. `pip install --upgrade pip`
1. `pip install poetry`
1. `poetry install`

<a id="examples"></a>
## Examples

This directory contains separate Python modules (code files) that run independently to demonstrate different features of the `decimal` package from the Python Standard Library (PSL) -- meaning that this is a built-in package that comes with the Python interpreter when you install it, and requires no additional dependencies.


<a id="references"></a>
## References

- ...

<a id="license"></a>
## License

See the [LICENSE](../LICENSE) file in the top-level directory for details.
