
# Reexporta funciones clave para una API más amigable
from .text import tokens_count, describe_length
from .numbers import safe_div, is_even

__all__ = ["tokens_count", "describe_length", "safe_div", "is_even"]
