import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("mundiales.csv")

# Limpieza opcional: reemplazar caracteres extraños en nombres de países
df['pais'] = df['pais'].str.encode('latin1').str.decode('utf-8', errors='ignore')

# Calcular partidos pendientes (por ejemplo, si se espera que juegue un mínimo de 114 como Brasil)
max_partidos = df['partidos_totales'].max()
df['partidos_pendientes'] = max_partidos - df['partidos_totales']

# Mostrar primeros datos
print("Resumen de datos por país:\n")
print(df[['pais', 'partidos_totales', 'partidos_ganados', 'partidos_empatados', 'partidos_perdidos', 'partidos_pendientes']].head())

# Crear gráfica de barras apiladas
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
