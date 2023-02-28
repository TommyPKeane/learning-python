# `decimal` Module of Python Standard Library

<!-- MarkdownTOC -->

- [Setup](#setup)
- [Examples](#examples)
    - [`decimal_features.py`](#decimal_featurespy)
    - [`precision_detail.py`](#precision_detailpy)
    - [`precision_simple.py`](#precision_simplepy)
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

This directory contains separate Python modules (code files) that run independently to demonstrate different features of the `decimal` package from the Python Standard Library (PSL) -- meaning that this is a built-in package that comes with the Python interpreter when you install it, and requires no additional dependencies.

<a id="decimal_featurespy"></a>
### `decimal_features.py`

Run the example with the following command:

```bash
python ./decimal_features.py
```

which should produce the output:

```
[TBD]
```

<a id="precision_detailpy"></a>
### `precision_detail.py`

Run the example with the following command:

```bash
python ./precision_detail.py
```

which should produce the output:

```
x: 3.1415926535897932384626433
y: 3.142
Precision 1 | Diff x - y: -0.0004

x: 3.1415926535897932384626433
y: 3.142
Precision 3 | Diff x - y: -0.000407

x: 3.1415926535897932384626433
y: 3.142
Precision 5 | Diff x - y: -0.00040735

x: 3.1415926535897932384626433
y: 3.142
Precision 12 | Diff x - y: -0.000407346410207
```


<a id="precision_simplepy"></a>
### `precision_simple.py`

Run the example with the following command:

```bash
python ./precision_simple.py
```

which should produce the output:

```
Precision 2: 3.1415926535897932384626433

Precision 10: 3.1415926535897932384626433

Precision 12 | Diff x - y: 0E-25

Precision 2 | Diff x - y: 0E-25

Precision 2: 3.141592

Precision 10: 3.141

Precision 12 | Diff x - y: 0.000592

Precision 2 | Diff x - y: 0.00059
```

<a id="license"></a>
## License

See the [LICENSE](../LICENSE) file in the top-level directory for details.
