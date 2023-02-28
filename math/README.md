# `math` Module of Python Standard Library

The Python Standard Library (PSL) includes a `math` package/module which supports numerous various mathematical calculations which the Python organization have determined are common enough in their use/necessity that they have been integrated into the interpreter directly.

Many convenience methods have been added throughout each iterative release of Python 3.x through PEP recommendations, which makes this PSL package an excellent basis for a custom Python mathematics package or library of your own design.

Note that there are methods here that may also be implemented in some of the other majorly popular scientific and computational Python packages, but these methods do not require any third-party dependencies, and may have certain other limitations or assumptions that do not necessarily align with those external packages. As always, if you're expecting any kind of rigor in your code, you need to diligently check the documentation and confirm that the assumptions are aligned. And, as one of the benefits of open-source languages or packages, you have the bonus ability to also review the source code and confirm that your understanding from the documentation is accurately reflected in the implementation.

Other Mathematics Packages outside of the PSL:
- https://numpy.org/ (`poetry add numpy`)
- https://scipy.org/ (`poetry add scipy`)
- https://scikit-learn.org/stable/ (`poetry add scikit-learn`)

<!-- MarkdownTOC -->

- [Setup](#setup)
- [Examples](#examples)
    - [`floating_point.py`](#floating_pointpy)
    - [`numbers.py`](#numberspy)
    - [`statistics.py`](#statisticspy)
- [References](#references)
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

<a id="floating_pointpy"></a>
### `floating_point.py`

Run the example with the following command:

```bash
python ./floating_point.py
```

which should produce the output:

```
[...]
```

<a id="numberspy"></a>
### `numbers.py`

The PSL `math` package includes numerical operations like `ceil()`, `floor()`, and `trunc()`, which are all ways to convert floating-point values to integers, and we can see how they vary from, or align to, one another by comparing their outputs with positive and negative values.

Run the example with the following command:

```bash
python ./numbers.py
```

which should produce the output:

```
x: 3.14159 | floor: 3 | trunc: 3 | ceil: 4
x: -3.14159 | floor: -4 | trunc: -3 | ceil: -3
x: 0.14159 | floor: 0 | trunc: 0 | ceil: 1
x: -0.14159 | floor: -1 | trunc: 0 | ceil: 0
x: 0.59 | floor: 0 | trunc: 0 | ceil: 1
x: -0.59 | floor: -1 | trunc: 0 | ceil: 0
```

<a id="statisticspy"></a>
### `statistics.py`

The PSL `math` package includes numerous statistical computations, like mathematical "combinations" and "permutations", which are ways of counting the number of `k`-tuples that can be selected from a universe of `n` elements with or without differentiating through ordering.

- `math.choose(n, k)` gives you `n Choose k` as the total number of "combinations" (`k`-tuples where ordering is ignored, thus `abc` is equivalent to `bac`, `cab`, `acb`, `cba`, and `bca`, and thus is only counted once).
- `math.perm(n, k)` gives you `n Permute k` as the total number of "permuations" (`k`-tuples where ordering is important, thus `abc`, `bac`, `cab`, `acb`, `cba`, and `bca` are all counted separately).

As such, this means that `math.perm(n, k) >= math.choose(n, k)` in general; which we can confirm by scripting up some examples to see the outputs.

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

<a id="references"></a>
## References

- https://en.wikipedia.org/wiki/Twelvefold_way
- https://en.wikipedia.org/wiki/Combination
- https://en.wikipedia.org/wiki/Permutation
- https://en.wikipedia.org/wiki/Floating-point_arithmetic
- https://en.wikipedia.org/wiki/Significand
- https://en.wikipedia.org/wiki/Common_logarithm
- https://en.wikipedia.org/wiki/Common_logarithm#Mantissa_and_characteristic

<a id="license"></a>
## License

See the [LICENSE](../LICENSE) file in the top-level directory for details.
