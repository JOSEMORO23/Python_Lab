from __future__ import annotations

def safe_div(a: float, b: float) -> float:
    """
    Realiza una división segura entre dos números flotantes.

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Returns:
        float: Resultado de la división.

    Raises:
        ZeroDivisionError: Si b es cero.
    """
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    return a / b

def is_even(n: int) -> bool:
    """
    Determina si un número entero es par.

    Args:
        n (int): Número a evaluar.

    Returns:
        bool: True si n es par, False en caso contrario.
    """
    return n % 2 == 0