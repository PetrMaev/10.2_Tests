import pytest

from src.calculate_tax import calculate_tax




def test_calculate_tax():
    assert calculate_tax(100, 10) == 110


def test_calculate_tax_invalid_price():
    with pytest.raises(ValueError):
        calculate_tax(-1, 20)


def test_calculate_tax_invalid_tax():
    with pytest.raises(ValueError):
        calculate_tax(100, -1)
