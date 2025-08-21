# main_paquete.py
from toolkit import tokens_count, describe_length, safe_div
import toolkit.numbers as num  # importación absoluta paquete.módulo

def run():
    s = "uno dos tres cuatro"
    print("tokens_count:", tokens_count(s))
    print("describe_length:", describe_length(s))
    print("safe_div(10, 2):", safe_div(10, 2))
    try:
        print("safe_div(1, 0):", num.safe_div(1, 0))
    except ZeroDivisionError as e:
        print("Error controlado:", e)

if __name__ == "__main__":
    run()
