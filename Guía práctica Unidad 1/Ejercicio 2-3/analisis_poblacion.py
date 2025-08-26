import pandas as pd
import matplotlib.pyplot as plt

def opcion_1():
  
    try:
        df = pd.read_csv("poblacionMunicipios.csv", sep=";", encoding="utf-8", on_bad_lines='skip')
    except Exception as e:
        print("Error al leer el archivo:", e)
        return

    print("Vista previa de los datos:")
    print(df.head())

    if 'Recaudacion' in df.columns and 'Provincia' in df.columns:
        df['Recaudacion'] = pd.to_numeric(df['Recaudacion'], errors='coerce')
        minimo = df["Recaudacion"].min()
        df["Recaudacion"].fillna(minimo, inplace=True)
        promedios = df.groupby("Provincia")["Recaudacion"].mean().reset_index()
        promedios = promedios.sort_values(by="Recaudacion", ascending=False)

        print("\nPromedio de recaudacion por provincia:")
        print(promedios)

        promedios.to_csv("promedio_recaudacion_provincia.csv", index=False)

        top10 = promedios.head(10)
        plt.figure(figsize=(10, 6))
        bars = plt.bar(top10["Provincia"], top10["Recaudacion"], color='skyblue')
        plt.xticks(rotation=45, ha='right')
        plt.title("Top 10 Provincias por Promedio de Recaudacion")
        plt.ylabel("Recaudacion Promedio (€)")
        plt.xlabel("Provincia")
        plt.tight_layout()

        for bar in bars:
            height = bar.get_height()
            plt.annotate(f"{height:.1f}", xy=(bar.get_x() + bar.get_width() / 2, height),
                         xytext=(0, 3), textcoords="offset points", ha='center', fontsize=9)
        plt.show()
    else:
        print("Las columnas 'Provincia' o 'Recaudacion' no existen en el archivo.")

def opcion_2():
    # --- Código del segundo ejercicio ---
    df = pd.read_csv("mundiales.csv")
    df['pais'] = df['pais'].str.encode('latin1').str.decode('utf-8', errors='ignore')
    max_partidos = df['partidos_totales'].max()
    df['partidos_pendientes'] = max_partidos - df['partidos_totales']

    print("Resumen de datos por país:\n")
    print(df[['pais', 'partidos_totales', 'partidos_ganados', 'partidos_empatados', 'partidos_perdidos', 'partidos_pendientes']].head())

    plt.figure(figsize=(14, 8))
    bar1 = plt.bar(df['pais'], df['partidos_ganados'], label='Ganados', color='green')
    bar2 = plt.bar(df['pais'], df['partidos_empatados'], bottom=df['partidos_ganados'], label='Empatados', color='gold')
    bar3 = plt.bar(df['pais'], df['partidos_perdidos'],
                   bottom=df['partidos_ganados'] + df['partidos_empatados'], label='Perdidos', color='red')
    bar4 = plt.bar(df['pais'], df['partidos_pendientes'],
                   bottom=df['partidos_ganados'] + df['partidos_empatados'] + df['partidos_perdidos'],
                   label='Pendientes', color='gray')

    plt.xticks(rotation=90)
    plt.ylabel("Número de partidos")
    plt.title("Total de partidos por equipo en los mundiales")
    plt.legend()
    plt.tight_layout()
    plt.show()

# --- Menú principal ---
while True:
    print("\n--- Menú ---")
    print("1. Analizar recaudación por provincia")
    print("2. Analizar partidos de mundiales")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == '1':
        opcion_1()
    elif opcion == '2':
        opcion_2()
    elif opcion == '3':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
