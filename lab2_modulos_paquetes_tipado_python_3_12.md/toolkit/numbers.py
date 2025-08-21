# toolkit/numbers.py
from __future__ import annotations

def safe_div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    return a / b

def is_even(n: int) -> bool:
    return n % 2 == 0
