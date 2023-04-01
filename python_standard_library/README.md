# Python Standard Library (PSL) Examples

This directory contains custom examples demonstrating the features and functionality in the Python Standard Library (PSL) using the latest stable release of Python.

<!-- MarkdownTOC -->

- [Setup](#setup)
- [Custom `python_standard_library` Package](#custom-python_standard_library-package)
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

<a id="custom-python_standard_library-package"></a>
## Custom `python_standard_library` Package

This repo contains a custom Python Package managed through `poetry` and named: `python_standard_library`. To demonstrate examples of the features of the Python Standard Library (PSL), we have a mix of custom modules/scripts and Unit-Testing.

The Unit-Testing can be run with:

```bash
pytest
```

Though, you'll only see the Code Coverage result; so you'll need to actually read through the `tests_unit/` directory structure to review the code to see and understand the examples. You can also add/modify the logging if you want to do some further introspection, or even put in some breakpoints in the tests and run the Python Debugger (`pdb`) if you want to step through the code as it gets interpreted in the runtime.

> 🤷‍♀️ 👻 🤓 _... I can't decide which approach is most useful to demonstrate and explain the Python Standard Library features, so I first made a bunch of scripts that just printed-out results, but now I've changed this to use Unit-Testing with `pytest` and `hypothesis`. I may end-up doing both, or also maybe setup Jupyter Lab for iPython Notebooks as another avenue of examples. We'll see what happens, so tag along for this extremely verbosely neurotically solipsisticly boring adventure! (The most tommy kind of adventure there is!)_

<a id="references"></a>
## References

- ...

<a id="license"></a>
## License

See the [LICENSE](../LICENSE) file in the top-level directory for details.
