import os
import time
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import pandas as pd
from io import BytesIO
from dotenv import load_dotenv
# Cargar variables de entorno desde el archivo .env
load_dotenv()

def procesar_archivos_parquet(ruta_directorio):
    """
    Función para procesar archivos Parquet en un directorio.

    Args:
    ruta_directorio (str): La ruta del directorio que contiene los archivos Parquet.

    Returns:
    list: Lista de nombres de archivos Parquet en el directorio.
    """
    archivos_parquet = []

    # Obtener la lista de nombres de archivos Parquet en el directorio
    archivos = os.listdir(ruta_directorio)

    # Filtrar los nombres de los archivos Parquet
    for archivo in archivos:
        if archivo.endswith('.parquet'):
            archivos_parquet.append(archivo)

    return archivos_parquet

def cargar_parquet_a_blob(archivo_parquet, ruta_directorio, account_name, account_key, container_name):
    """
    Función para cargar un archivo Parquet en Azure Blob Storage.

    Args:
    archivo_parquet (str): Nombre del archivo Parquet que se desea cargar.
    ruta_directorio (str): La ruta del directorio que contiene el archivo Parquet.
    account_name (str): El nombre de la cuenta de almacenamiento.
    account_key (str): La clave de la cuenta de almacenamiento.
    container_name (str): El nombre del contenedor Blob.

    Returns:
    None
    """
    # Generar la ruta completa del archivo Parquet
    ruta_completa = os.path.join(ruta_directorio, archivo_parquet)

    # Generar la ruta de destino en el contenedor Blob
    #ruta_destino_blob = f"raw-data/yellow_analytics/{archivo_parquet}"
    ruta_destino_blob = f"raw-data/yellow_analytics/{archivo_parquet}"
    # Conexión a la cuenta de almacenamiento
    blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

    # Verificar si el archivo ya existe en el contenedor Blob
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(ruta_destino_blob)

    try:
        blob_properties = blob_client.get_blob_properties()
        print(f"El archivo {archivo_parquet} ya existe en el contenedor de Azure Blob Storage. No se volverá a cargar.")
    except Exception as ex:
        # Si el blob no existe, cargar el archivo
        df = pd.read_parquet(ruta_completa)
        
        # Subir archivo al contenedor
        with BytesIO() as bytes_io:
            df.to_parquet(bytes_io)
            blob_client.upload_blob(bytes_io.getvalue(), overwrite=True)
        
        print(f"Archivo {archivo_parquet} cargado exitosamente en Azure Blob Storage.")


def cargar_datos_parquet(ruta_directorio, account_name, account_key, container_name):
    """
    Función para procesar y cargar archivos Parquet en Azure Blob Storage,
    y guardar un registro de tiempo en un archivo de texto.

    Args:
    ruta_directorio (str): La ruta del directorio que contiene los archivos Parquet.
    account_name (str): El nombre de la cuenta de almacenamiento.
    account_key (str): La clave de la cuenta de almacenamiento.
    container_name (str): El nombre del contenedor Blob.

    Returns:
    None
    """
    try:
        # Registro de tiempo de inicio
        inicio = time.time()

        # Obtener la lista de nombres de archivos Parquet en el directorio
        archivos_parquet = procesar_archivos_parquet(ruta_directorio)

        # Iterar sobre cada archivo Parquet
        for archivo_parquet in archivos_parquet:
            # Cargar el archivo Parquet en Azure Blob Storage
            cargar_parquet_a_blob(archivo_parquet, ruta_directorio, account_name, account_key, container_name)
            # Esperar 10 segundos antes de procesar el siguiente archivo
            time.sleep(10)

            # Registro de tiempo de finalización
            fin = time.time()

            # Calcular la duración total de la ejecución
            duracion = fin - inicio

            # Crear la carpeta logs y controles si no existe
            carpeta_controles = os.path.join("logs", "controles")
            if not os.path.exists(carpeta_controles):
                os.makedirs(carpeta_controles)

            # Guardar el registro en un archivo de texto
            with open(os.path.join(carpeta_controles, "loaddata_logs.txt"), "w") as f:
                f.write(f"Tiempo de inicio: {inicio}\n")
                f.write(f"Tiempo de finalización: {fin}\n")
                f.write(f"Duración total (segundos): {duracion}\n")

    except Exception as e:
        print(f"Error al cargar los datos Parquet: {e}")


# Ejemplo de uso de la función
#ruta_directorio = r'C:\Users\ozi\ti\MVP_ML_TransporteNY\datasets\processed\yellow_analytics'
ruta_directorio = r'C:\Users\ozi\ti\MVP_ML_TransporteNY\datasets\processed\yellow_analytics'
account_name = os.getenv("ACCOUNT_NAME")
account_key = os.getenv("ACCOUNT_KEY")
container_name = 'getdatalakefiles'

# Llamar a la función para procesar y cargar archivos Parquet en Azure Blob Storage
cargar_datos_parquet(ruta_directorio, account_name, account_key, container_name)
