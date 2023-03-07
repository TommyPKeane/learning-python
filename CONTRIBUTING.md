#  How to Use this Repository

Each directory of any runnable/testable collection of code in this repo should have a `README.md` file which should have sections dedicated to how to actually run or use the code.

But if you're looking at this repo for the first time and want to make sure your system is all set on how to work with the code and test or run any of it, this document provides a generic overall set of details on how to confirm that your system is setup, and explains some of the DevOps and design decisions we've made in this repository.

There are numerous ways to run or manage Python code, so if you already are familiar with them, you may be able to use your own preferences. This just explains what I've done here, and why I've chosen this approach. I'm always open to learning about a new way, so if you know of something I should be doing instead and you wanna share/discuss it, feel free to reach out :smile:.

<!-- MarkdownTOC -->

- [Common Setup](#common-setup)
    - [Why Not Docker?](#why-not-docker)

<!-- /MarkdownTOC -->


<a id="common-setup"></a>
## Common Setup

This repo relies on `pyenv` and `direnv` to create directory-local "projects", which establish a fixed, local instance of Python to use as an isolated interpreter (runtime) where we can keep all our dependencies isolated.

The major benefit of this approach is that we avoid the disconnect of Docker, and enforces an encapsulated development environment that can be shared between developers and more easily productionalized _via_ Docker or some other deployment.

In macOS you can setup the tools with `brew` using the following commands:

- `brew install direnv`
- `brew install pyenv`

In each project directory there will be four common files:

- `.python-version`: Version of Python (per `pyenv`) in use
- `.envrc`: `direnv` Configuration File
- `pyproject.toml`: Project and Package Dependencies Management
- `poetry.toml`: Poetry Configuration Options
- `poetry.lock`: Dependency Lock File (hashes etc.)

As such, you'll note that almost all the `.envrc` configuration files for `direnv` look like this:

```bash
# direnv Config File
#
# https://direnv.net/
# https://github.com/pyenv/pyenv

python_version=$(cat "./.python-version")

layout pyenv "${python_version}"
```

As a pre-cursor to calling `direnv allow`, you should make sure that you have the appropriate version of Python installed through `pyenv` by calling `pyenv install` in the same directory as the `.python-version` file.

The common setup steps for each directory will follow this sequence:

1. `pyenv install` (Optional)
1. `direnv allow`
1. `pip install --upgrade pip`
1. `pip install poetry`
1. `poetry install`

Arguably, you can install a system-level version of `poetry`, to avoid incremental updates, similar to `direnv` and `pyenv`, but that's really only going to be a consideration in a team-based development environment or in professional software when you need to prioritize stability and repeatability.

Another alternative to a system-level version of `poetry` is also to just enforce a version constraint when you install `poetry` by using a command like `pip install poetry==1.2.3`, where `1.2.3` is the version you want to "lock" your Project to.

<a id="why-not-docker"></a>
### Why Not Docker?

What's with `direnv` and `pyenv`? Do you really need those? Why not just work directly in Docker?

You can, if you want -- you can do anything you want, I'm definitely not in charge 👻.

If you're asking why would I suggest avoiding Docker, I'd say that there's a complexity of system resource management, caching, publishing, and logging that are all complicated by using Docker. These are things that can all be overcome, even if they're innate to a Dockerized deployment, but that's where the effort should be focused on the deployment itself and not necessarily the code/app being deployed.

It's essentially a recommendation for a "separation of duties". If you think about writing a book, you have the content of the book (the text), but then you also have the typography and typesetting/layout of how the book is paginated and ultimately printed. As best as possible, it's beneficial to separate those two things, so that you can just focus on content and then worry about presentation afterwards. Things can go very wrong if you overly "tie" your content to your media/medium, because then it's not a separable and configurable presentation layer, it's then a fundamental assumption/requirement of the content itself.

Obviously, we can't solve everything, so we have to pick and choose our battles. So, in that sense, in my experience, there's a nice happy middle-ground by developing in Python with `direnv`, `pyenv`, and `poetry`, and then using Docker or some other system runtime management tooling to establish the production version.
