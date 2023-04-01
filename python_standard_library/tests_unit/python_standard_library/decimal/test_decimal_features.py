import decimal
import logging

import pytest

# from python_standard_library.decimal.decimal_features import *


module_log = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "string",
    (
        "3,141,592.653_589".replace(",", "_"),
        "3.141_592_653_589_793_238_462_643_3",
        "3.142",
    ),
)
def test_Decimal_str(string: str) -> None:
    dec: decimal.Decimal = decimal.Decimal(string)
    assert isinstance(dec, decimal.Decimal)
    assert dec is not None
    return None


@pytest.mark.parametrize(
    "string",
    (
        "3,141,592.653_589",
        "3'141'592'653'589'793'238'462'643'3",
        "ThreePointOneFourOneFiveNine",
        "two",
    ),
)
def test_Decimal_str_bad(string: str) -> None:
    with pytest.raises(decimal.InvalidOperation):
        dec: decimal.Decimal = decimal.Decimal(string)
    return None
