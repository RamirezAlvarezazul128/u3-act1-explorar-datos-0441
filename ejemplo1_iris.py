import pandas as pd
import os
# Ramirez Azul NC 0441
# URL del dataset público leer datos de iris.cvs
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# Descargar y cargar el CSV
datos = pd.read_csv(url)

# print(datos)
# Guardar una copia local
datos.to_csv("datasets/iris.csv", index=False)

# Explorar los datos
print("PRIMERAS 5 FILAS")
print(datos.head())
print()
print("\\nCANTIDAD DE FILAS Y COLUMNAS")
print(datos.shape)

print("Mostrando nombre de las columnas")
print("\\nNOMBRES DE LAS COLUMNAS")
print(datos.columns.tolist())

print("\\nINFORMACION DEL DATASET (conjunto de datos)")
print(datos.info())
print("\\nCARACTERISTICAS (X) tumba la columna especies con drop")
X = datos.drop(columns=["species"])
print(X.head())
print("\\nVARIABLE OBJETIVO (y)")
y = datos["species"]
print(y.head())
print("\\nESPECIES REGISTRADAS con la opcion unica")
print(y.unique())