# Notas — Parte A (Módulos)

**API pública de `string_utils`:**
- `normalize_text(text)`: Normaliza removiendo diacríticos y colapsando espacios.
- `is_valid_email(email)`: Valida formato básico de correo.
- `slugify(text, max_len=60)`: Crea un slug URL-safe.
- `truncate_safe(text, max_len)`: Trunca sin partir palabras; lanza `ValueError` si `max_len<1`.

**¿Por qué separarlo en un módulo?**
- Agrupa utilidades coherentes de cadenas.
- Facilita pruebas y reutilización desde otros scripts.
- Reduce acoplamiento del punto de entrada.


# Notas — Parte B (Paquetes)

**Absolutas vs. relativas**
- **Absolutas** (`import paquete.modulo` / `from paquete import x`): claras y estables para uso externo o desde scripts principales.
- **Relativas** (`from .otro_modulo import x`): útiles dentro del mismo paquete para evitar dependencias frágiles de nombres de proyecto.

**Qué expone `toolkit/__init__.py` y por qué**
- Reexporta `tokens_count`, `describe_length`, `safe_div`, `is_even` para una API plana y simple (`from toolkit import ...`).
