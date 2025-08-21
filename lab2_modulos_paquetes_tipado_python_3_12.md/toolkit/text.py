# toolkit/text.py
from __future__ import annotations
from .numbers import is_even  # importación relativa dentro del paquete

def tokens_count(s: str) -> int:
    return len(s.split())

def describe_length(s: str) -> str:
    n = len(s)
    return f"len={n} (par)" if is_even(n) else f"len={n} (impar)"
