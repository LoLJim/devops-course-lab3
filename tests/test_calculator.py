"""Тесты для модуля калькулятора."""

import pytest

from calculator import add, subtract, multiply, divide, power, modulo


def test_add() -> None:
    """Проверка сложения."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract() -> None:
    """Проверка вычитания."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply() -> None:
    """Проверка умножения."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0


def test_divide() -> None:
    """Проверка деления."""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    with pytest.raises(ValueError):
        divide(1, 0)


def test_power() -> None:
    """Проверка возведения в степень."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_modulo() -> None:
    """Проверка остатка от деления."""
    assert modulo(17, 5) == 2
    assert modulo(10, 3) == 1
    with pytest.raises(ValueError):
        modulo(5, 0)
