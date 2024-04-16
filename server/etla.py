import dask.dataframe as dd
from dask.distributed import Client, LocalCluster
import os
from datetime import datetime
import re
import time

def optimize_and_process_dataframe(df):
    # Definir las columnas a eliminar
    columnas_a_eliminar = ['store_and_fwd_flag', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 'congestion_surcharge', 'airport_fee', 'Airport_fee']

    # Verificar si las columnas a eliminar existen antes de intentar eliminarlas
    for col in columnas_a_eliminar:
        if col in df.columns:
            df = df.drop(columns=col)

    df = df.dropna()
    # Filtrar por los años 2022 y 2023 en las columnas de fecha
    df = df[(df['tpep_pickup_datetime'].dt.year.isin([2022, 2023])) & (df['tpep_dropoff_datetime'].dt.year.isin([2022, 2023]))]
    # Eliminar filas con valores nulos del DataFrame de Dask

    # Convertir las columnas de fechas a tipo DateTime en Dask
    for col in ['tpep_pickup_datetime', 'tpep_dropoff_datetime']:
        df[col] = dd.to_datetime(df[col])

    # Agregar columnas para fechas y hora_minutos 
    for col in ['tpep_pickup_datetime', 'tpep_dropoff_datetime']:
        df[col + '_fecha'] = df[col].dt.strftime('%Y-%m-%d')
        df[col + '_hora'] = df[col].dt.strftime('%H').astype('int32')  # Formatear como HH:MM:SS

    # Calcular la duración del viaje en segundos
    df['DuracionViaje'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds()

    # Filtrar registros que no cumplen con las condiciones
    df = df[(df['RatecodeID'] > 1) & (df['RatecodeID'] <= 6)]
    df = df[(df['DuracionViaje'] > 310) & (df['DuracionViaje'] <= 2700)]
    df = df[(df['passenger_count'] > 0) & (df['passenger_count'] <= 4)]
    df = df[(df['trip_distance'] > 0.5) & (df['trip_distance'] <= 13)]
    df = df[(df['total_amount'] > 11.3) & (df['total_amount'] <= 50.25)]

    # Eliminar las columnas originales de fecha y hora
    df = df.drop(['tpep_pickup_datetime', 'tpep_dropoff_datetime'], axis=1)

    # Convertir passenger_count y DuracionViaje a enteros
    df['passenger_count'] = df['passenger_count'].astype(int)
    df['DuracionViaje'] = df['DuracionViaje'].astype(int)

    # Definir mapeo de nombres de columnas a nuevos nombres
    new_column_names = {
        "VendorID": "IdProveedor",
        "passenger_count": "TotalPasajeros",
        "trip_distance": "DistanciaViaje",
        "RatecodeID": "IdTipoTarifa",
        "PULocationID": "IdZonaOrigen",
        "DOLocationID": "IdZonaDestino",
        "payment_type": "IdTipoPago",
        "total_amount": "CostoTotal",
        "tpep_pickup_datetime_fecha": "FechaRecogida",
        "tpep_pickup_datetime_hora": "HoraRecogida",
        "tpep_dropoff_datetime_fecha": "FechaLlegada",
        "tpep_dropoff_datetime_hora": "HoraLlegada"
    }

    # Renombrar las columnas del DataFrame de Dask
    df = df.rename(columns=new_column_names)

    # Eliminar las columnas que tienen la información unificada de Fecha y Hora
    df.drop(columns=['FechaLlegada'], inplace=True)
    df.drop(columns=['HoraLlegada'], inplace=True)

    # Eliminamos los datos superiores a 6, porque el diccionario establece solo datos del 1-6
    df.drop(df[df['IdTipoTarifa'] > 6].index, inplace=True)

    return df

def is_processed(file_name):
    try:
        with open(os.path.join("logs", "controles", "processed_files.txt"), "r") as processed_log:
            processed_files = processed_log.read().splitlines()
            if file_name in processed_files:
                return True
            else:
                return False
    except Exception as e:
        print(f"Error al verificar el estado del archivo: {e}")
        return False

def main():
    # Registro de hora de inicio
    start_time = datetime.now()

    # Configurar el clúster de Dask
    with LocalCluster(n_workers=2, threads_per_worker=1, memory_limit='6GB') as cluster, \
        Client(cluster) as client:

        # Imprimir la información sobre el clúster
        print(f"Clúster de Dask iniciado con {len(cluster.workers)} trabajadores.")

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

        # Verificar cuántos archivos se han procesado
        try:
            with open(os.path.join("logs", "controles", "processed_files.txt"), "r") as processed_log:
                processed_files = processed_log.read().splitlines()
        except FileNotFoundError:
            processed_files = []

        # Iterar sobre la lista de archivos filtrados
        for i, archivo in enumerate(archivos_filtrados):
            if archivo not in processed_files:
                # Definir la ruta completa del archivo Parquet
                ruta_parquet = os.path.join("..", "datasets", "raw", archivo)

                # Cargar los datos en un DataFrame distribuido de Dask y particionarlo
                df_dask = dd.read_parquet(ruta_parquet, engine='pyarrow')
                df_dask_particionado = df_dask.repartition(npartitions=4)

                # Aplicar el procesamiento avanzado a cada partición y escribir en Parquet
                for j, particion in enumerate(df_dask_particionado.to_delayed()):
                    df_particion_procesado = optimize_and_process_dataframe(particion.compute())

                    # Crear un archivo Parquet a partir de cada partición
                    ruta_salida = os.path.join("..", "datasets", "processed", "yellow_analytics", f"yellow_analytics_part_{i+1}_{j+1}.parquet")
                    df_particion_procesado.to_parquet(ruta_salida, engine='pyarrow')

                    # Registrar el archivo como procesado
                    with open(os.path.join("logs", "controles", "processed_files.txt"), "a") as processed_log:
                        processed_log.write(f"{archivo}\n")

                    # Esperar 10 segundos antes de iniciar el siguiente archivo
                    time.sleep(10)
                    print(f"Terminó ETL del archivo {i+1}, iniciando el archivo {i+2}...")

    # Registro de hora de finalización y duración del proceso
    end_time = datetime.now()
    duration = end_time - start_time

    # Escribir en el archivo de logs
    with open(os.path.join("..", "controles", "etl_logs.txt"), "a") as log_file:
        log_file.write(f"Inicio: {start_time}, Fin: {end_time}, Duración: {duration}\n")

if __name__ == "__main__":
    main()
