# Python 3.13 | Custom Package with `uv`

This folder is an example of creating and managing your own custom Python Package with `uv`, supported by `direnv`, `pyenv`, and `pytest`.

`uv` (package/project manager) is made by the same team who makes `ruff` (linter and formatter).

<!-- MarkdownTOC -->

- [Environment Setup and Install](#environment-setup-and-install)
    - [Updating `ruff` and other `uv` Tools](#updating-ruff-and-other-uv-tools)
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

And then you can install `uv` and `ruff` (via `uv`) with:

```bash
brew install uv
```

then

```bash
uv tool install ruff
```

and then make sure the tools are in your `PATH` with

```bash
uv tool update-shell
```

and then if you're using `bash` you can make sure your shell is updated in the current terminal session with:

```bash
source ~/.bashrc
```

<a id="updating-ruff-and-other-uv-tools"></a>
### Updating `ruff` and other `uv` Tools

When you install a "tool" with `ruff`, you won't be managing it directly through `brew`, so the `brew` steps for updates won't work:

1. `brew update`
1. `brew upgrade`

instead, you would use the following to update `ruff`:

```bash
uv tool upgrade ruff
```

<a id="developer-setup"></a>
## Developer Setup

> ***Last Tested with:***
> - `uv 0.8.17 (Homebrew 2025-09-10)`
> - `ruff 0.13.0`


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
1. Install the Python dependencies and setup the local Package with `uv` by relying on the already active `direnv` and `pyenv` local virtual environment:
    ```bash
    uv sync --active
    ```

`uv` recommends to use their built-in `venv` management for Virtual Environments, but with this example we're showing how to rely on `direnv` and `pyenv`, which can be a bit more featureful and stable as `uv` is still in active development.

This also allows you to compare/contrast this setup and the processes with a similar setup using `poetry` also shown in this repository for `poetry` version `v1.8` and `poetry` version `v2.0`, as there are some nuanced differences between all three of these approaches.

<a id="references"></a>
## References

- https://docs.astral.sh/uv/
- https://docs.astral.sh/ruff/
- https://docs.astral.sh/uv/concepts/projects/dependencies/
