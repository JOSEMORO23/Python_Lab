
#Paso 1: Revisión de datos
# Importar la libreria Pandas
import pandas as pd

#Recupero el archivo de data etiquetada
atributos = ['Class-Name', 'handicapped-infants', 'water-project-cost-sharing',
'adoption-of-the-budget-resolution', 'physician-fee-freeze',
'el-salvador-aid', 're-groups-in-schools', 'anti-satellite-test-ban',
'aid-to-nicaraguan-contras', 'mx-missile', 'immigration',
'synfuels-corporation-cutback', 'education-spending', 'superfund-right-to-sue',
'crime', 'duty-free-exports', 'export-administration-act-south-africa']
df_datos=pd.read_csv('house-votes-84.data.txt', sep=',', index_col='Class-Name', names=atributos)
print(df_datos.head(6))

[] #Paso 2
#Reemplazo de datos correpondientes de y,n y ?. y significa que votaron por ese candidato (1)
#n significa que no votaron por el candidato(0)
#? significa que votaron en blanco (3), en el testo se indica que (?) no significa desconocido, signifca otro valor,
df_datos = df_datos.replace('n','0')
df_datos = df_datos.replace('y', '1')
df_datos = df_datos.replace('?','3')
df_datos.describe()

#Paso 3
#Se Determina el conjunto de modelización y el de validación, para esto se utiliza train_test_split indicando que
#Breserve las proporciones de Dataframe orginal
#El bloque de entrenamiento es el 75% de los registros, y al bloque de pruebas el 25% restante
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
X_train, X_test, y_train, y_test = train_test_split(df_datos, df_datos.index, random_state=1, stratify = df_datos.index)
#Se verifica los tamaños de los datos originales, de entrenamiento y test
print("\nNumero de datos total", df_datos.shape[0])
print("Numero de datos para Entrenamiento 75%", X_train.shape[0])
print("Numero de datos para Test 25%", X_test.shape[0])
#Se analiza que se mantengan los porcentajes de clasificación de lo datos del originar, entrenamiento y test agrupado por Cla
print(" Porcetnaje Original ")
print(df_datos.groupby("Class-Name").count()/len(df_datos))
print(" Porcentaje entrenamiento ")
print(X_train.groupby("Class-Name").count()/len(X_train))
print(" Porcentaje Test ")
print(X_test.groupby("Class-Name").count()/len(X_test))