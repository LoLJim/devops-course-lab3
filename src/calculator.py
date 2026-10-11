

def add(a: float, b: float) -> float:
    """Сложение двух чисел."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Вычитание двух чисел."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""
    return a * b


def divide(a: float, b: float) -> float:
    """Деление двух чисел."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    """Возведение в степень."""
    return a ** b


def modulo(a: float, b: float) -> float:
    """Остаток от деления."""
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
