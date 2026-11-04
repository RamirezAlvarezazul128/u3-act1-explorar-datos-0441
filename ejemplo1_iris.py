import pandas as pd
import os
# Ramirez Azul NC 0441
# URL del dataset público leer datos de iris.cvs
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# Descargar y cargar el CSV
datos = pd.read_csv(url)

print(datos)
# Guardar una copia local
datos.to_csv("datasets/iris.cvs, index=False")

# Explorar los datos
print("PRIMERAS 5 FILAS")
print(datos.head())
print()
print("\\nCANTIDAD DE FILAS Y COLUMNAS")
print(datos.shape)