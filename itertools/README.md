# `itertools` Module of Python Standard Library

<!-- MarkdownTOC -->

- [Setup](#setup)
- [Examples](#examples)
    - [`permutations.py`](#permutationspy)
- [`iterable_operators.py`](#iterable_operatorspy)
- [`mixed_iterators.py`](#mixed_iteratorspy)
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

This directory contains separate Python modules (code files) that run independently to demonstrate different features of the `itertools` package from the Python Standard Library (PSL) -- meaning that this is a built-in package that comes with the Python interpreter when you install it, and requires no additional dependencies.

<a id="permutationspy"></a>
### `permutations.py`

Run the example with the following command:

```bash
python ./permutations.py
```

which should produce the output:

```bash
>> Processing Iterable: HELLO

Full-Length Permutations (Unique Orderings, No Replacement, N=5): ['HELLO', 'HELOL', 'HELLO', 'HELOL', 'HEOLL', 'HEOLL',
'HLELO', 'HLEOL', 'HLLEO', 'HLLOE', 'HLOEL', 'HLOLE', 'HLELO', 'HLEOL', 'HLLEO', 'HLLOE', 'HLOEL', 'HLOLE', 'HOELL',
'HOELL', 'HOLEL', 'HOLLE', 'HOLEL', 'HOLLE', 'EHLLO', 'EHLOL', 'EHLLO', 'EHLOL', 'EHOLL', 'EHOLL', 'ELHLO', 'ELHOL',
'ELLHO', 'ELLOH', 'ELOHL', 'ELOLH', 'ELHLO', 'ELHOL', 'ELLHO', 'ELLOH', 'ELOHL', 'ELOLH', 'EOHLL', 'EOHLL', 'EOLHL',
'EOLLH', 'EOLHL', 'EOLLH', 'LHELO', 'LHEOL', 'LHLEO', 'LHLOE', 'LHOEL', 'LHOLE', 'LEHLO', 'LEHOL', 'LELHO', 'LELOH',
'LEOHL', 'LEOLH', 'LLHEO', 'LLHOE', 'LLEHO', 'LLEOH', 'LLOHE', 'LLOEH', 'LOHEL', 'LOHLE', 'LOEHL', 'LOELH', 'LOLHE',
'LOLEH', 'LHELO', 'LHEOL', 'LHLEO', 'LHLOE', 'LHOEL', 'LHOLE', 'LEHLO', 'LEHOL', 'LELHO', 'LELOH', 'LEOHL', 'LEOLH',
'LLHEO', 'LLHOE', 'LLEHO', 'LLEOH', 'LLOHE', 'LLOEH', 'LOHEL', 'LOHLE', 'LOEHL', 'LOELH', 'LOLHE', 'LOLEH', 'OHELL',
'OHELL', 'OHLEL', 'OHLLE', 'OHLEL', 'OHLLE', 'OEHLL', 'OEHLL', 'OELHL', 'OELLH', 'OELHL', 'OELLH', 'OLHEL', 'OLHLE',
'OLEHL', 'OLELH', 'OLLHE', 'OLLEH', 'OLHEL', 'OLHLE', 'OLEHL', 'OLELH', 'OLLHE', 'OLLEH']

Full-Length Combinations (Unique Sub-Sets, N=5): ['HELLO']

Full-Length Combinations with Replacement (Unique Orderings, N=5): ['HHHHH', 'HHHHE', 'HHHHL', 'HHHHL', 'HHHHO', 'HHHEE',
'HHHEL', 'HHHEL', 'HHHEO', 'HHHLL', 'HHHLL', 'HHHLO', 'HHHLL', 'HHHLO', 'HHHOO', 'HHEEE', 'HHEEL', 'HHEEL', 'HHEEO',
'HHELL', 'HHELL', 'HHELO', 'HHELL', 'HHELO', 'HHEOO', 'HHLLL', 'HHLLL', 'HHLLO', 'HHLLL', 'HHLLO', 'HHLOO', 'HHLLL',
'HHLLO', 'HHLOO', 'HHOOO', 'HEEEE', 'HEEEL', 'HEEEL', 'HEEEO', 'HEELL', 'HEELL', 'HEELO', 'HEELL', 'HEELO', 'HEEOO',
'HELLL', 'HELLL', 'HELLO', 'HELLL', 'HELLO', 'HELOO', 'HELLL', 'HELLO', 'HELOO', 'HEOOO', 'HLLLL', 'HLLLL', 'HLLLO',
'HLLLL', 'HLLLO', 'HLLOO', 'HLLLL', 'HLLLO', 'HLLOO', 'HLOOO', 'HLLLL', 'HLLLO', 'HLLOO', 'HLOOO', 'HOOOO', 'EEEEE',
'EEEEL', 'EEEEL', 'EEEEO', 'EEELL', 'EEELL', 'EEELO', 'EEELL', 'EEELO', 'EEEOO', 'EELLL', 'EELLL', 'EELLO', 'EELLL',
'EELLO', 'EELOO', 'EELLL', 'EELLO', 'EELOO', 'EEOOO', 'ELLLL', 'ELLLL', 'ELLLO', 'ELLLL', 'ELLLO', 'ELLOO', 'ELLLL',
'ELLLO', 'ELLOO', 'ELOOO', 'ELLLL', 'ELLLO', 'ELLOO', 'ELOOO', 'EOOOO', 'LLLLL', 'LLLLL', 'LLLLO', 'LLLLL', 'LLLLO',
'LLLOO', 'LLLLL', 'LLLLO', 'LLLOO', 'LLOOO', 'LLLLL', 'LLLLO', 'LLLOO', 'LLOOO', 'LOOOO', 'LLLLL', 'LLLLO', 'LLLOO',
'LLOOO', 'LOOOO', 'OOOOO']

Full-Length Cross-Product ("HELLO" x "HELLO"): ['HH', 'HE', 'HL', 'HL', 'HO', 'EH', 'EE', 'EL', 'EL', 'EO', 'LH', 'LE',
'LL', 'LL', 'LO', 'LH', 'LE', 'LL', 'LL', 'LO', 'OH', 'OE', 'OL', 'OL', 'OO']



>> Processing Iterable: HELLO

Variable-Length Permutations (Unique Orderings, No Replacement, N=[1, 2, 3, 4, 5]): ['H', 'E', 'L', 'L', 'O', 'HE', 'HL', 'HL',
'HO', 'EH', 'EL', 'EL', 'EO', 'LH', 'LE', 'LL', 'LO', 'LH', 'LE', 'LL', 'LO', 'OH', 'OE', 'OL', 'OL', 'HEL', 'HEL', 'HEO',
'HLE', 'HLL', 'HLO', 'HLE', 'HLL', 'HLO', 'HOE', 'HOL', 'HOL', 'EHL', 'EHL', 'EHO', 'ELH', 'ELL', 'ELO', 'ELH', 'ELL',
'ELO', 'EOH', 'EOL', 'EOL', 'LHE', 'LHL', 'LHO', 'LEH', 'LEL', 'LEO', 'LLH', 'LLE', 'LLO', 'LOH', 'LOE', 'LOL', 'LHE',
'LHL', 'LHO', 'LEH', 'LEL', 'LEO', 'LLH', 'LLE', 'LLO', 'LOH', 'LOE', 'LOL', 'OHE', 'OHL', 'OHL', 'OEH', 'OEL', 'OEL',
'OLH', 'OLE', 'OLL', 'OLH', 'OLE', 'OLL', 'HELL', 'HELO', 'HELL', 'HELO', 'HEOL', 'HEOL', 'HLEL', 'HLEO', 'HLLE', 'HLLO',
'HLOE', 'HLOL', 'HLEL', 'HLEO', 'HLLE', 'HLLO', 'HLOE', 'HLOL', 'HOEL', 'HOEL', 'HOLE', 'HOLL', 'HOLE', 'HOLL', 'EHLL',
'EHLO', 'EHLL', 'EHLO', 'EHOL', 'EHOL', 'ELHL', 'ELHO', 'ELLH', 'ELLO', 'ELOH', 'ELOL', 'ELHL', 'ELHO', 'ELLH', 'ELLO',
'ELOH', 'ELOL', 'EOHL', 'EOHL', 'EOLH', 'EOLL', 'EOLH', 'EOLL', 'LHEL', 'LHEO', 'LHLE', 'LHLO', 'LHOE', 'LHOL', 'LEHL',
'LEHO', 'LELH', 'LELO', 'LEOH', 'LEOL', 'LLHE', 'LLHO', 'LLEH', 'LLEO', 'LLOH', 'LLOE', 'LOHE', 'LOHL', 'LOEH', 'LOEL',
'LOLH', 'LOLE', 'LHEL', 'LHEO', 'LHLE', 'LHLO', 'LHOE', 'LHOL', 'LEHL', 'LEHO', 'LELH', 'LELO', 'LEOH', 'LEOL', 'LLHE',
'LLHO', 'LLEH', 'LLEO', 'LLOH', 'LLOE', 'LOHE', 'LOHL', 'LOEH', 'LOEL', 'LOLH', 'LOLE', 'OHEL', 'OHEL', 'OHLE', 'OHLL',
'OHLE', 'OHLL', 'OEHL', 'OEHL', 'OELH', 'OELL', 'OELH', 'OELL', 'OLHE', 'OLHL', 'OLEH', 'OLEL', 'OLLH', 'OLLE', 'OLHE',
'OLHL', 'OLEH', 'OLEL', 'OLLH', 'OLLE', 'HELLO', 'HELOL', 'HELLO', 'HELOL', 'HEOLL', 'HEOLL', 'HLELO', 'HLEOL', 'HLLEO',
'HLLOE', 'HLOEL', 'HLOLE', 'HLELO', 'HLEOL', 'HLLEO', 'HLLOE', 'HLOEL', 'HLOLE', 'HOELL', 'HOELL', 'HOLEL', 'HOLLE',
'HOLEL', 'HOLLE', 'EHLLO', 'EHLOL', 'EHLLO', 'EHLOL', 'EHOLL', 'EHOLL', 'ELHLO', 'ELHOL', 'ELLHO', 'ELLOH', 'ELOHL',
'ELOLH', 'ELHLO', 'ELHOL', 'ELLHO', 'ELLOH', 'ELOHL', 'ELOLH', 'EOHLL', 'EOHLL', 'EOLHL', 'EOLLH', 'EOLHL', 'EOLLH',
'LHELO', 'LHEOL', 'LHLEO', 'LHLOE', 'LHOEL', 'LHOLE', 'LEHLO', 'LEHOL', 'LELHO', 'LELOH', 'LEOHL', 'LEOLH', 'LLHEO',
'LLHOE', 'LLEHO', 'LLEOH', 'LLOHE', 'LLOEH', 'LOHEL', 'LOHLE', 'LOEHL', 'LOELH', 'LOLHE', 'LOLEH', 'LHELO', 'LHEOL',
'LHLEO', 'LHLOE', 'LHOEL', 'LHOLE', 'LEHLO', 'LEHOL', 'LELHO', 'LELOH', 'LEOHL', 'LEOLH', 'LLHEO', 'LLHOE', 'LLEHO',
'LLEOH', 'LLOHE', 'LLOEH', 'LOHEL', 'LOHLE', 'LOEHL', 'LOELH', 'LOLHE', 'LOLEH', 'OHELL', 'OHELL', 'OHLEL', 'OHLLE',
'OHLEL', 'OHLLE', 'OEHLL', 'OEHLL', 'OELHL', 'OELLH', 'OELHL', 'OELLH', 'OLHEL', 'OLHLE', 'OLEHL', 'OLELH', 'OLLHE',
'OLLEH', 'OLHEL', 'OLHLE', 'OLEHL', 'OLELH', 'OLLHE', 'OLLEH']



>> Processing Iterable: [1, 2, 3, 4]

Full-Length Permutations (Unique Orderings, No Replacement, N=4): ['1234', '1243', '1324', '1342', '1423', '1432', '2134',
'2143', '2314', '2341', '2413', '2431', '3124', '3142', '3214', '3241', '3412', '3421', '4123', '4132', '4213', '4231', '4312',
'4321']

Full-Length Combinations (Unique Sub-Sets, N=4): ['1234']

Full-Length Combinations with Replacement (Unique Orderings, N=4): ['1111', '1112', '1113', '1114', '1122', '1123', '1124',
'1133', '1134', '1144', '1222', '1223', '1224', '1233', '1234', '1244', '1333', '1334', '1344', '1444', '2222', '2223',
'2224', '2233', '2234', '2244', '2333', '2334', '2344', '2444', '3333', '3334', '3344', '3444', '4444']

Full-Length Cross-Product ("[1, 2, 3, 4]" x "[1, 2, 3, 4]"): ['11', '12', '13', '14', '21', '22', '23', '24', '31', '32',
'33', '34', '41', '42', '43', '44']



>> Processing Iterable: [1, 2, 3, 4]

Variable-Length Permutations (Unique Orderings, No Replacement, N=[1, 2, 3, 4]): ['1', '2', '3', '4', '12', '13', '14', '21',
'23', '24', '31', '32', '34', '41', '42', '43', '123', '124', '132', '134', '142', '143', '213', '214', '231', '234', '241',
'243', '312', '314', '321', '324', '341', '342', '412', '413', '421', '423', '431', '432', '1234', '1243', '1324', '1342',
'1423', '1432', '2134', '2143', '2314', '2341', '2413', '2431', '3124', '3142', '3214', '3241', '3412', '3421', '4123',
'4132', '4213', '4231', '4312', '4321']
```

<a id="iterable_operatorspy"></a>
## `iterable_operators.py`

Run the example with the following command:

```bash
python ./iterable_operators.py
```

which should produce the output:

```bash
>> Example Iterable: [1, 2, 3, 5, 7, 9, 11, 13]
>> Cumulative Summation (cumsum): [1, 3, 6, 11, 18, 27, 38, 51]
>> Custom Accumulation (i + j - 2): [1, 1, 2, 5, 10, 17, 26, 37]
>> Drop first N Values as long as they adhere to custom check (x < 10): [11, 13]
>> Keep first N Values as long as they adhere to custom check (x < 10): [1, 2, 3, 5, 7, 9]
>> Keep any Values that adhere to the custom check (x < 10): [1, 2, 3, 5, 7, 9]
>> Keep any Values that DO NOT adhere to the custom check (x < 10): [11, 13]


>> Example Iterable: [1, 2, 3, 5, 7, 9, 11, 13, 11, 12, 10, 9, 8, 7, 6]
>> Cumulative Summation (cumsum): [1, 3, 6, 11, 18, 27, 38, 51, 62, 74, 84, 93, 101, 108, 114]
>> Custom Accumulation (i + j - 2): [1, 1, 2, 5, 10, 17, 26, 37, 46, 56, 64, 71, 77, 82, 86]
>> Drop first N Values as long as they adhere to custom check (x < 10): [11, 13, 11, 12, 10, 9, 8, 7, 6]
>> Keep first N Values as long as they adhere to custom check (x < 10): [1, 2, 3, 5, 7, 9]
>> Keep any Values that adhere to the custom check (x < 10): [1, 2, 3, 5, 7, 9, 9, 8, 7, 6]
>> Keep any Values that DO NOT adhere to the custom check (x < 10): [11, 13, 11, 12, 10]
```

<a id="mixed_iteratorspy"></a>
## `mixed_iterators.py`

Run the example with the following command:

```bash
python ./mixed_iterators.py
```

which should produce the output:

```bash
>> Zipping: "HELLO" and "YOU"
>> Fill Character for Mismatched Lengths: "_"
>> Result of itertools.zip_longest(): ['HY', 'EO', 'LU', 'L_', 'O_']

>> Zipping: "YOU" and "HELLO"
>> Fill Character for Mismatched Lengths: "_"
>> Result of itertools.zip_longest(): ['YH', 'OE', 'UL', '_L', '_O']

>> Zipping: "[1, 2, 3]" and "['A', 'B', 'C', 'D']"
>> Fill Character for Mismatched Lengths: "_"
>> Result of itertools.zip_longest(): ['1A', '2B', '3C', '_D']
>> Result after dropping trailing pairing: ['1A', '2B', '3C']
>> Compared to normal zip(): ['1A', '2B', '3C']
```

<a id="references"></a>
## References

- https://docs.python.org/3/library/itertools.html

<a id="license"></a>
## License

See the [LICENSE](../LICENSE) file in the top-level directory for details.
