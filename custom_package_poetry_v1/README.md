# Python 3.13 | Custom Package with `poetry` (version `v1.8.z`)

This folder is an example of creating and managing your own custom Python Package with `poetry`, supported by `direnv`, `pyenv`, and `pytest`.

<!-- MarkdownTOC -->

- [Environment Setup and Install](#environment-setup-and-install)
- [Developer Setup](#developer-setup)
- [References](#references)

<!-- /MarkdownTOC -->


<a id="environment-setup-and-install"></a>
## Environment Setup and Install

On macOS or Linux if using `brew` (https://brew.sh), you can install `direnv` and `pyenv` with the commands:

```bash
brew install direnv
```

and

```bash
brew install pyenv
```

And if you want a full compilation/install for Python, you'd likely also want to make sure you use `brew` to install these libraries:

- `brew install gcc`
- `brew install openssl`
- `brew install zlib`
- `brew install make`
- `brew install cmake`
- `brew install readline`
- `brew install tcl-tk`
- `brew install ncurses`

<a id="developer-setup"></a>
## Developer Setup

1. Make sure you have the Python Version installed:
    ```bash
    pyenv install
    ```
1. Create the local Project Environment:
    ```bash
    direnv allow
    ```
1. Confirm your Python executable is in the local `.direnv` directory:
    ```bash
    which python
    ```
1. Make sure the latest version of `pip` is installed:
    ```bash
    pip install --upgrade pip
    ```
1. Install the Python dependencies and setup the local Package with `poetry`:
    ```bash
    pip install "poetry<2"
    ```

<a id="references"></a>
## References

- https://python-poetry.org/docs/1.8/
- https://docs.astral.sh/ruff/
