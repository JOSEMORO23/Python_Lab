# usar_string_utils.py
from string_utils import normalize_text, is_valid_email, slugify, truncate_safe

def demo():
    print("== normalize_text ==")
    print(normalize_text("  Café   con   Leche "))
    print()

    print("== is_valid_email ==")
    for e in ["jose@mail.com", "no-es-email", "x@y"]:
        print(e, "=>", is_valid_email(e))
    print()

    print("== slugify ==")
    print(slugify("¡Hola Mundo desde Python !"))
    print()

    print("== truncate_safe (con caso límite) ==")
    print(truncate_safe("Esto es una frase bastante larga para cortar bien.", 20))
    try:
        # Caso límite que debe fallar de forma controlada
        print(truncate_safe("texto", 0))
    except ValueError as exc:
        print("Error controlado:", exc)

if __name__ == "__main__":
    demo()
