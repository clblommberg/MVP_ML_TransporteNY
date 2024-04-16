import dask.dataframe as dd
from dask.distributed import Client, LocalCluster
import os
from datetime import datetime
import re
import time


def procesamiento_avanzado_particion(df):
    # Filtrar y eliminar columnas no deseadas
    columnas_a_eliminar = ['originating_base_num', 'access_a_ride_flag', 'wav_request_flag', 
                           'wav_match_flag', 'shared_request_flag', 'shared_match_flag',
                           'access_a_ride_flag']
    df = df.drop(columnas_a_eliminar, axis=1)
    
    # Reemplazar valores nulos por 0.00 en columnas relevantes
    relevant_columns = ['base_passenger_fare', 'tolls', 'bcf', 'sales_tax', 'congestion_surcharge',
                        'airport_fee', 'tips', 'driver_pay']
    df = df.fillna({col: 0.00 for col in relevant_columns})

    # Calcular la columna 'total_amount' sumando las columnas relevantes
    df['total_amount'] = df[relevant_columns].sum(axis=1)

    # Eliminar columnas no deseadas
    columnas_a_eliminar = ['tolls', 'bcf', 'sales_tax', 'congestion_surcharge', 
                           'airport_fee', 'tips', 'driver_pay']
    df = df.drop(columnas_a_eliminar, axis=1)

    # Filtrar por los años 2022 y 2023 en las columnas de fecha
    df = df[(df['pickup_datetime'].dt.year.isin([2022, 2023])) & (df['dropoff_datetime'].dt.year.isin([2022, 2023]))]
    # Filtrar por los años 2022 y 2023 en las columnas de fecha
    df = df[(df['request_datetime'].dt.year.isin([2022, 2023])) & (df['on_scene_datetime'].dt.year.isin([2022, 2023]))]
    # Eliminar filas con valores nulos del DataFrame de Dask
    # Convertir columnas de fechas a tipo DateTime en Dask
    for col in ['pickup_datetime', 'dropoff_datetime', 'request_datetime', 'on_scene_datetime']:
        df[col] = dd.to_datetime(df[col])

    # Agregar columnas para fechas, horas, minutos y segundos
    for col in ['pickup_datetime', 'dropoff_datetime', 'request_datetime', 'on_scene_datetime']:
        df[col + '_fecha'] = df[col].dt.strftime('%Y-%m-%d')
        df[col + '_hora_minuto'] = df[col].dt.strftime('%H:%M')  # Formatear como HH:MM
        
    # Calcular la duración del viaje y de espera en segundos
    df['DuracionAtencion'] = (df['on_scene_datetime'] - df['request_datetime']).dt.total_seconds()

    # Eliminar filas con duraciones negativas o nulas
    df = df[df['DuracionAtencion'] >= 0]
    
    # Eliminar columnas originales
    df = df.drop(columns=['pickup_datetime', 'dropoff_datetime', 'request_datetime', 'on_scene_datetime'])

    # Renombrar las columnas del DataFrame de Dask
    new_column_names = {
        "hvfhs_license_num": "IdApp",
        "dispatching_base_num": "IdProveedor",
        "PULocationID": "IdZonaOrigen",
        "DOLocationID": "IdZonaDestino",
        "trip_miles": "DistanciaViaje",
        "base_passenger_fare": "TarifaPasajero",
        "pickup_datetime_fecha": "FechaRecogida",
        "pickup_datetime_hora_minuto": "HoraRecogida",
        "dropoff_datetime_fecha": "FechaLlegada",
        "dropoff_datetime_hora_minuto": "HoraLlegada",
        "request_datetime_fecha": "FechaSolicitada",
        "request_datetime_hora_minuto": "HoraSolicitada",
        "on_scene_datetime_fecha": "FechaAtendida",
        "on_scene_datetime_hora_minuto": "HoraAtendida",
        "total_amount": "CostoTotal"
    }
    df = df.rename(columns=new_column_names)

    return df

def main():
    # Registro de hora de inicio
    start_time = datetime.now()

    # Configurar el clúster de Dask
    with LocalCluster(n_workers=2, threads_per_worker=1, memory_limit='12GB') as cluster, \
        Client(cluster) as client:

        # Imprimir la información sobre el clúster
        print(f"Clúster de Dask iniciado con {len(cluster.workers)} trabajadores.")

        # Ruta del directorio que contiene los archivos
        ruta_directorio = r'C:\Users\ozi\ti\MVP_ML_TransporteNY\datasets\raw'

        # Expresión regular para el nombre de los archivos
        patron = r'^fhvhv_tripdata_202[2-3]-\d{2}\.parquet$'

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
            with open(os.path.join("logs", "controles", "processed_filesb.txt"), "r") as processed_log:
                processed_files = processed_log.read().splitlines()
        except FileNotFoundError:
            processed_files = []

        # Iterar sobre la lista de archivos filtrados
        for i, archivo in enumerate(archivos_filtrados):
            if archivo not in processed_files:
                # Definir la ruta completa del archivo Parquet
                ruta_parquet = os.path.join(ruta_directorio, archivo)

                # Cargar los datos en un DataFrame distribuido de Dask y particionarlo
                df_dask = dd.read_parquet(ruta_parquet, engine='pyarrow')
                df_dask_particionado = df_dask.repartition(npartitions=4)

                # Aplicar el procesamiento avanzado a cada partición y escribir en Parquet
                for j, particion in enumerate(df_dask_particionado.to_delayed()):
                    df_particion_procesado = procesamiento_avanzado_particion(particion.compute())

                    # Crear un archivo Parquet a partir de cada partición
                    ruta_salida = os.path.join("..", "datasets", "processed", "ffvh_analytics", f"ffvh_analytics_part_{i}_{j+1}.parquet")
                    df_particion_procesado.to_parquet(ruta_salida, engine='pyarrow')

                    # Registro de hora de finalización y duración del proceso
                    end_time = datetime.now()
                    duration = end_time - start_time

                    # Escribir en el archivo de logs
                    with open(os.path.join("logs","controles", "etlb_logs.txt"), "a") as log_file:
                        log_file.write(f"Archivo procesado: {archivo}, Inicio: {start_time}, Fin: {end_time}, Duración: {duration}\n")

                    # Registrar el archivo como procesado
                    with open(os.path.join("logs", "controles", "processed_filesb.txt"), "a") as processed_log:
                        processed_log.write(f"{archivo}\n")

                    # Esperar 10 segundos antes de iniciar el siguiente archivo
                    time.sleep(10)
                    print(f"Terminó ETL del archivo {i+1}, iniciando el archivo {i+2}...")

                # Actualizar el tiempo de inicio para el próximo archivo
                start_time = datetime.now()

if __name__ == "__main__":
    main()
