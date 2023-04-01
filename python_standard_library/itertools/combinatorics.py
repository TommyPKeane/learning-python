import itertools


def show_combinatorics_comparisons(iterable, num_elements):
    print(f">> Processing Iterable: {iterable}")
    print()

    permutations: list[str] = ["".join(map(str, tpl)) for tpl in itertools.permutations(iterable, num_elements)]
    print(f"Full-Length Permutations (Unique Orderings, No Replacement, N={num_elements}): {permutations}")
    print()

    combinations: list = ["".join(map(str, tpl)) for tpl in itertools.combinations(iterable, num_elements)]
    print(f"Full-Length Combinations (Unique Sub-Sets, N={num_elements}): {combinations}")
    print()

    combinations_with_replacement: list = [
        "".join(map(str, tpl)) for tpl in itertools.combinations_with_replacement(iterable, num_elements)
    ]
    print(f"Full-Length Combinations with Replacement (Unique Orderings, N={num_elements}): {combinations_with_replacement}")
    print()

    cross_product: list = ["".join(map(str, tpl)) for tpl in itertools.product(iterable, iterable)]
    print(f"Full-Length Cross-Product (\"{iterable}\" x \"{iterable}\"): {cross_product}")
    print()
    print()
    print()

    return;


def show_combinatorics_all_subset_permutations(iterable, max_length: int, min_length: int = 1):
    permutations = []
    permutation_sizes = range(min_length, max_length + 1, 1)

    for subset_length in permutation_sizes:
        permutations.extend(
            ["".join(map(str, tpl)) for tpl in itertools.permutations(iterable, subset_length)]
        )

    print(f">> Processing Iterable: {iterable}")
    print()

    print(f"Variable-Length Permutations (Unique Orderings, No Replacement, N={list(permutation_sizes)}): {permutations}")
    print()
    print()
    print()

    return permutations


if __name__ == "__main__":
    example_iterable: str = "HELLO"
    num_elements: int = len(example_iterable)
    show_combinatorics_comparisons(example_iterable, num_elements)
    show_combinatorics_all_subset_permutations(example_iterable, max_length=num_elements, min_length=1)


    example_iterable: list[int] = [1, 2, 3, 4]
    num_elements: int = len(example_iterable)
    show_combinatorics_comparisons(example_iterable, num_elements)
    show_combinatorics_all_subset_permutations(example_iterable, max_length=num_elements, min_length=1)
