import itertools


if __name__ == "__main__":
    example_iterable = [1, 2, 3, 5, 7, 9, 11, 13]

    print(f">> Example Iterable: {example_iterable}")

    cumsum = list(itertools.accumulate(example_iterable))
    print(f">> Cumulative Summation (cumsum): {cumsum}")

    custom_accumulation = list(itertools.accumulate(example_iterable, lambda i,j: i + j - 2))
    print(f">> Custom Accumulation (i + j - 2): {custom_accumulation}")

    after_values = list(itertools.dropwhile(lambda x: x < 10, example_iterable))
    print(f">> Drop first N Values as long as they adhere to custom check (x < 10): {after_values}")

    before_values = list(itertools.takewhile(lambda x: x < 10, example_iterable))
    print(f">> Keep first N Values as long as they adhere to custom check (x < 10): {before_values}")

    print()
    print()

    example_iterable = [1, 2, 3, 5, 7, 9, 11, 13, 11, 12, 10, 9, 8, 7, 6]

    print(f">> Example Iterable: {example_iterable}")

    cumsum = list(itertools.accumulate(example_iterable))
    print(f">> Cumulative Summation (cumsum): {cumsum}")

    custom_accumulation = list(itertools.accumulate(example_iterable, lambda i,j: i + j - 2))
    print(f">> Custom Accumulation (i + j - 2): {custom_accumulation}")

    after_values = list(itertools.dropwhile(lambda x: x < 10, example_iterable))
    print(f">> Drop first N Values as long as they adhere to custom check (x < 10): {after_values}")

    before_values = list(itertools.takewhile(lambda x: x < 10, example_iterable))
    print(f">> Keep first N Values as long as they adhere to custom check (x < 10): {before_values}")
