"""
ДЗ презентации 4, повышенный уровень, задача 1.
Время: 25–35 минут.

Тема: Decimal, ROUND_HALF_UP.

Условие:
    Запросите цену (строка, например "19.99"), количество
    и налоговую ставку в процентах. Вычислите итоговую стоимость
    с помощью Decimal, округлив до двух знаков по ROUND_HALF_UP.

Пример:
    In: 19.99
    In: 3
    In: 13
    Out: Overall: 67.77
"""
import decimal
from decimal import Decimal, ROUND_HALF_UP


def total(price: str, qty: int, tax: str) -> str:
    no_tax = Decimal(f'{price}') * Decimal(f'{qty}')
    stupid_tax = Decimal(price)/100 * Decimal(tax)
    all = Decimal(no_tax) + Decimal(stupid_tax)*Decimal(qty)

    return f'Overall: {all.quantize(Decimal('0.01'), rounding = decimal.ROUND_HALF_UP)}'


if __name__ == "__main__":
    assert total("19.99", 3, "13") == "Overall: 67.77"
    assert total("100", 1, "0") == "Overall: 100.00"
    print("task_01 (p4 advanced): тесты пройдены")
