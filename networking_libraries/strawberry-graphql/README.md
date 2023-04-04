# GraphQL Examples in Python 3.11 with `strawberry-graphql`

The [`strawberry-graphql`](https://strawberry.rocks/) Package is a third-party Python package (library) that provides Python utility classes and methods for supporting the construction and parsing of GraphQL Queries/Requests.

[GraphQL](https://en.wikipedia.org/wiki/GraphQL) is an alternative API standard/format, in contrast to [REST(ful)](https://en.wikipedia.org/wiki/Representational_state_transfer) APIs, though both operate over HTTP requests.

<!-- MarkdownTOC -->

- [Setup](#setup)
- [References](#references)

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

<a id="references"></a>
## References

- https://strawberry.rocks/
- https://github.com/strawberry-graphql/strawberry
- https://www.contentful.com/blog/graphql-via-http-in-five-ways/
- https://graphql.org/learn/serving-over-http/
