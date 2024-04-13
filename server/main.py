from scrapy import DatasetDownloader
from etl import main as etl_main
from loaddata import cargar_datos_parquet
import os
from dotenv import load_dotenv
# Cargar variables de entorno desde el archivo .env
load_dotenv()

def main():
    try:
        # Descargar los conjuntos de datos
        base_url = 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
        download_folder = '..\\datasets\\raw'
        downloader = DatasetDownloader(base_url, download_folder)
        downloader.download_datasets()

        # Ejecutar la ETL
        etl_main()

        # Cargar datos Parquet en Azure Blob Storage y registrar tiempo
        ruta_directorio = r'C:\Users\ozi\ti\MVP_ML_TransporteNY\datasets\processed\yellow_analytics'

        # Obtener los valores de las variables de entorno
        account_name = os.getenv("ACCOUNT_NAME")
        account_key = os.getenv("ACCOUNT_KEY")
        container_name = 'getdatalakefiles'
        cargar_datos_parquet(ruta_directorio, account_name, account_key, container_name)
    except Exception as e:
        print(f"Error en el proceso: {e}")

if __name__ == "__main__":
    main()
