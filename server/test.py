import os
import dask.dataframe as dd
import re
# Ruta del directorio que contiene los archivos
ruta_directorio = r'C:\Users\ozi\ti\MVP_ML_TransporteNY\datasets\raw'

# Expresión regular para el nombre de los archivos
patron = r'^yellow_tripdata_202[2-3]-\d{2}\.parquet$'

# Lista para almacenar los nombres de los archivos filtrados
archivos_filtrados = []

# Obtener la lista de todos los archivos en el directorio
archivos = os.listdir(ruta_directorio)

# Filtrar los nombres de los archivos
for archivo in archivos:
    if re.match(patron, archivo):
        archivos_filtrados.append(archivo)

# Imprimir los nombres de los archivos filtrados
for archivo_filtrado in archivos_filtrados:
    print(archivo_filtrado)