import logging
import math

import pytest

# from python_standard_library.math.statistics import *


module_log = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "n, k, expected_result",
    (
        (12, 3, 220),
        (2, 1, 2),
        (365, 3, 8_038_030),
        (33, 34, 0),
    ),
)
def test_comb(n: int, k: int, expected_result: int) -> None:
    n_choose_k = math.comb(n, k)
    assert n_choose_k == expected_result
    return None


@pytest.mark.parametrize(
    "n, k, expected_result",
    (
        (12, 3, 1_320),
        (2, 1, 2),
        (365, 3, 48_228_180),
        (33, 34, 0),
    ),
)
def test_perm(n: int, k: int, expected_result: int) -> None:
    n_perm_k = math.perm(n, k)
    assert n_perm_k == expected_result
    return None
