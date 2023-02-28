# Examples of Statistics Calculations from the PSL `math` Package
#
# References:
# - https://docs.python.org/3/library/math.html
import math


def log_n_choose_k(n, k):
    n_choose_k = math.comb(n, k)
    print(f"n ({n:,d}) Choose k ({k:,d}): {n_choose_k:,d}")
    print(f"There are {n_choose_k:,d} possible {k:,d}-tuple combinations (unordered sets) from {n:,d} elements")
    print()  # Blank Line
    return n_choose_k


def log_n_perm_k(n, k):
    n_perm_k = math.perm(n, k)
    print(f"n ({n:,d}) perm k ({k:,d}): {n_perm_k:,d}")
    print(f"There are {n_perm_k:,d} possible {k:,d}-tuple permutations (ordered sets) from {n:,d} elements")
    print()  # Blank Line
    return n_perm_k


if __name__ == "__main__":
    n = 12
    k = 3
    n_choose_k = log_n_choose_k(n, k)

    n = 2
    k = 1
    n_choose_k = log_n_choose_k(n, k)

    n = 365
    k = 3
    n_choose_k = log_n_choose_k(n, k)

    n = 33
    k = 34
    n_choose_k = log_n_choose_k(n, k)

    n = 12
    k = 3
    n_perm_k = log_n_perm_k(n, k)

    n = 2
    k = 1
    n_perm_k = log_n_perm_k(n, k)

    n = 365
    k = 3
    n_perm_k = log_n_perm_k(n, k)

    n = 33
    k = 34
    n_perm_k = log_n_perm_k(n, k)
