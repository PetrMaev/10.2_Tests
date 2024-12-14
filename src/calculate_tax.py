def calculate_tax(price: float, tax_rate: float, discount: float = 0) -> float:
    for arg in [price, tax_rate, discount]:
        if not isinstance(arg, int | float):
            raise TypeError("Неверный формат данных")

    if price < 0:
        raise ValueError("Неверная цена")

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError("Неверный налоговый процент")

    return round(price + (price * tax_rate / 100) - price * discount / 100, 2)


print(calculate_tax(100, 20.00, 10))
