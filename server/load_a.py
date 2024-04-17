import os
import time
import pandas as pd
from io import BytesIO
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError
from dotenv import load_dotenv
# Cargar variables de entorno desde el archivo .env
load_dotenv()

def procesar_archivos_parquet(ruta_directorio):
    archivos_parquet = []
    archivos = os.listdir(ruta_directorio)
    for archivo in archivos:
        if archivo.endswith('.parquet'):
            archivos_parquet.append(archivo)
    return archivos_parquet


def cargar_parquet_a_blob(archivo_parquet, ruta_directorio, account_name, account_key, container_name):
    ruta_completa = os.path.join(ruta_directorio, archivo_parquet)
    ruta_destino_blob = f"raw-data/yellow_analytics/{archivo_parquet}"

    blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(ruta_destino_blob)

    try:
        blob_properties = blob_client.get_blob_properties()
        print(f"El archivo {archivo_parquet} ya existe en el contenedor de Azure Blob Storage. No se volverá a cargar.")
    except ResourceNotFoundError:
        try:
            df = pd.read_parquet(ruta_completa)
            return df
        except Exception as ex:
            print(f"Error al cargar el archivo {archivo_parquet} en Azure Blob Storage: {ex}")

def estratificar_muestra(df, columna, proporcion):
    """
    Realiza muestreo estratificado en un DataFrame según una columna específica.

    Parameters:
    - df (pd.DataFrame): El DataFrame de origen.
    - columna (str): El nombre de la columna sobre la que se realizará el muestreo estratificado.
    - proporcion (float): La proporción deseada de la muestra respecto al tamaño del DataFrame original. Por defecto, 0.12.

    Returns:
    - pd.DataFrame: DataFrame con la muestra estratificada.
    """
    # Calcular el tamaño de muestra proporcional para cada categoría en la columna especificada
    proporciones = df[columna].value_counts(normalize=True) * proporcion
    tamaño_muestra_por_categoria = (proporciones * len(df)).astype(int)

    # Lista para almacenar las muestras aleatorias estratificadas
    muestras_estratificadas = []

    # Iterar sobre cada categoría única en la columna especificada
    for categoria in df[columna].unique():
        # Seleccionar aleatoriamente el tamaño de muestra proporcional para la categoría actual
        muestra_categoria = df[df[columna] == categoria].sample(tamaño_muestra_por_categoria[categoria])
        # Agregar las muestras seleccionadas al DataFrame de muestras estratificadas
        muestras_estratificadas.append(muestra_categoria)

    # Concatenar las muestras estratificadas en un solo DataFrame
    muestras_estratificadas = pd.concat(muestras_estratificadas)

    return muestras_estratificadas

def cargar_y_estratificar_parquet(archivo_parquet, ruta_directorio, account_name, account_key, container_name):
    try:
        df = cargar_parquet_a_blob(archivo_parquet, ruta_directorio, account_name, account_key, container_name)
        if df is not None:
            df_estratificada = estratificar_muestra(df, columna='IdProveedor', proporcion=0.75)
            return df_estratificada
    except Exception as ex:
        print(f"Error al cargar y estratificar el archivo {archivo_parquet}: {ex}")

def procesar_archivos_y_cargar_blob(ruta_directorio, account_name, account_key, container_name):
    archivos_parquet = procesar_archivos_parquet(ruta_directorio)
    for archivo_parquet in archivos_parquet:
        try:
            df_estratificada = cargar_y_estratificar_parquet(archivo_parquet, ruta_directorio, account_name, account_key, container_name)
            if df_estratificada is not None:
                ruta_completa = os.path.join(ruta_directorio, archivo_parquet)
                ruta_destino_blob = f"raw-data/yellow_analytics/{archivo_parquet}"
                blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
                container_client = blob_service_client.get_container_client(container_name)
                blob_client = container_client.get_blob_client(ruta_destino_blob)

                with BytesIO() as bytes_io:
                    df_estratificada.to_parquet(bytes_io)
                    blob_client.upload_blob(bytes_io.getvalue(), overwrite=True)
                print(f"Archivo {archivo_parquet} cargado exitosamente en Azure Blob Storage.")
        except Exception as ex:
            print(f"Error al procesar y cargar el archivo {archivo_parquet}: {ex}")

# Ejemplo de uso
ruta_directorio = r'C:\Users\ozi\ti\MVP_ML_TransporteNY\datasets\processed\yellow_analytics'
account_name = os.getenv("ACCOUNT_NAME")
account_key = os.getenv("ACCOUNT_KEY")
container_name = 'getdatalakefiles'

procesar_archivos_y_cargar_blob(ruta_directorio, account_name, account_key, container_name)
