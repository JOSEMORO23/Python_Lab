# string_utils.py
"""
Utilidades de cadenas: normalización, validación y formato.
API pública:
- normalize_text(text)
- is_valid_email(email)
- slugify(text, max_len=60)
- truncate_safe(text, max_len)
"""

from __future__ import annotations
import re
import unicodedata

__all__ = ["normalize_text", "is_valid_email", "slugify", "truncate_safe"]

def normalize_text(text: str) -> str:
    """Quita acentos/diacríticos y colapsa espacios."""
    if not isinstance(text, str):
        raise TypeError("text debe ser str")
    nfkd = unicodedata.normalize("NFKD", text)
    sin_diacriticos = "".join(c for c in nfkd if not unicodedata.combining(c))
    colapsado = " ".join(sin_diacriticos.strip().split())
    return colapsado

_EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def is_valid_email(email: str) -> bool:
    """Valida formato simple de email (no verifica existencia)."""
    if not isinstance(email, str):
        return False
    return bool(_EMAIL_RE.match(email))

def slugify(text: str, max_len: int = 60) -> str:
    """Convierte texto en slug URL-safe."""
    base = normalize_text(text).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return slug[:max_len] or "n-a"

def truncate_safe(text: str, max_len: int) -> str:
    """Corta sin partir palabras cuando es posible. Lanza si max_len<1."""
    if max_len < 1:
        raise ValueError("max_len debe ser >= 1")
    if len(text) <= max_len:
        return text
    corte = text.rfind(" ", 0, max_len)
    return (text[:corte] if corte != -1 else text[:max_len]).rstrip() + "…"
