import pytest

from src.calc_taxes import calculate_taxes

@pytest.fixture
def prices():
    return [50, 100, 200]

@pytest.mark.parametrize("tax_rate, expected", [(10, [55, 110, 220]),
                                                 (15, [57.5, 115, 230]),
                                                (20, [60, 120, 240])                                                 ])


def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected


def test_calculate_taxes_invalid_prices():
    with pytest.raises(ValueError):
        calculate_taxes([0.0, -1.0], 20.0)


def test_calculate_taxes_invalid_taxes(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, -1.0)
