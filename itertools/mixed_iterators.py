import itertools


if __name__ == "__main__":
    long_iterable: str = "HELLO"
    short_iterable: str = "YOU"
    fill_char: str = "_"

    zipped_strings: list[str] = [
        "".join(map(str, tpl))  # Safety Enforce Strings for `.join()`
        for tpl
        in itertools.zip_longest(long_iterable, short_iterable, fillvalue=fill_char)
    ]
    print(f">> Zipping: \"{long_iterable}\" and \"{short_iterable}\"")
    print(f">> Fill Character for Mismatched Lengths: \"{fill_char}\"")
    print(f">> Result of itertools.zip_longest(): {zipped_strings}")
    print()

    zipped_strings: list[str] = [
        "".join(map(str, tpl))  # Safety Enforce Strings for `.join()`
        for tpl
        in itertools.zip_longest(short_iterable, long_iterable, fillvalue=fill_char)
    ]
    print(f">> Zipping: \"{short_iterable}\" and \"{long_iterable}\"")
    print(f">> Fill Character for Mismatched Lengths: \"{fill_char}\"")
    print(f">> Result of itertools.zip_longest(): {zipped_strings}")
    print()


    long_iterable: str = [1, 2, 3]
    short_iterable: str = ["A", "B", "C", "D"]
    fill_char: str = "_"

    zipped_strings: list[str] = [
        "".join(map(str, tpl))  # Safety Enforce Strings for `.join()`
        for tpl
        in itertools.zip_longest(long_iterable, short_iterable, fillvalue=fill_char)
    ]
    print(f">> Zipping: \"{long_iterable}\" and \"{short_iterable}\"")
    print(f">> Fill Character for Mismatched Lengths: \"{fill_char}\"")
    print(f">> Result of itertools.zip_longest(): {zipped_strings}")
    print(f">> Result after dropping trailing pairing: {[string for string in zipped_strings if fill_char not in string]}")
    print()
