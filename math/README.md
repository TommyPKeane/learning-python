# `math` Module of Python Standard Library

<!-- MarkdownTOC -->

- [Setup](#setup)
- [Examples](#examples)
    - [`numbers.py`](#numberspy)
    - [`statistics.py`](#statisticspy)
- [License](#license)

<!-- /MarkdownTOC -->

<a id="setup"></a>
## Setup

1. `pyenv install` (Optional)
1. `direnv allow`
1. `pip install --upgrade pip`
1. `pip install poetry`
1. `poetry install`

<a id="examples"></a>
## Examples

This directory contains separate Python modules (code files) that run independently to demonstrate different features of the `math` package from the Python Standard Library (PSL) -- meaning that this is a built-in package that comes with the Python interpreter when you install it, and requires no additional dependencies.

<a id="numberspy"></a>
### `numbers.py`

Run the example with the following command:

```bash
python ./numbers.py
```

which should produce the output:

```
[TBD]
```

<a id="statisticspy"></a>
### `statistics.py`

Run the example with the following command:

```bash
python ./statistics.py
```

which should produce the output:

```
n (12) Choose k (3): 220
There are 220 possible 3-tuple combinations (unordered sets) from 12 elements

n (2) Choose k (1): 2
There are 2 possible 1-tuple combinations (unordered sets) from 2 elements

n (365) Choose k (3): 8,038,030
There are 8,038,030 possible 3-tuple combinations (unordered sets) from 365 elements

n (33) Choose k (34): 0
There are 0 possible 34-tuple combinations (unordered sets) from 33 elements

n (12) perm k (3): 1,320
There are 1,320 possible 3-tuple permutations (ordered sets) from 12 elements

n (2) perm k (1): 2
There are 2 possible 1-tuple permutations (ordered sets) from 2 elements

n (365) perm k (3): 48,228,180
There are 48,228,180 possible 3-tuple permutations (ordered sets) from 365 elements

n (33) perm k (34): 0
There are 0 possible 34-tuple permutations (ordered sets) from 33 elements
```

<a id="license"></a>
## License

See the [LICENSE](../LICENSE) file in the top-level directory for details.
