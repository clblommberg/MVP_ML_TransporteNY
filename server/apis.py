import openmeteo_requests
import requests_cache
from retry_requests import retry
import pandas as pd
from pathlib import Path
import os
from sodapy import Socrata
import pandas as pd
from ckanapi import RemoteCKAN
import re
from unidecode import unidecode


class WeatherDataProcessor:
    def __init__(self, latitude, longitude, start_date, end_date, weather_variables):
        self.latitude = latitude
        self.longitude = longitude
        self.start_date = start_date
        self.end_date = end_date
        self.weather_variables = weather_variables

    def fetch_weather_data(self):
        """
        Fetches weather data from the Open-Meteo API.

        Returns:
        - list: List of responses from the API.
        """
        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        openmeteo = openmeteo_requests.Client(session=retry_session)

        # Construir los parámetros de la solicitud
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "hourly": self.weather_variables
        }

        # Realizar la solicitud a la API de Open-Meteo
        url = "https://archive-api.open-meteo.com/v1/archive"
        responses = openmeteo.weather_api(url, params=params)

        return responses

    def process_weather_data(self, response):
        """
        Processes weather data obtained from the Open-Meteo API.

        Args:
        - response: Response obtained from the API.

        Returns:
        - DataFrame: Processed DataFrame containing weather data.
        """
        # Procesar la respuesta
        response_data = response[0]
        print(f"Coordinates {response_data.Latitude()}°N {response_data.Longitude()}°E")
        print(f"Elevation {response_data.Elevation()} m asl")
        print(f"Timezone {response_data.Timezone()} {response_data.TimezoneAbbreviation()}")
        print(f"Timezone difference to GMT+0 {response_data.UtcOffsetSeconds()} s")

        # Procesar los datos meteorológicos por hora
        hourly = response_data.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {"date": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        )}
        hourly_data["temperature_2m"] = hourly_temperature_2m

        hourly_dataframe = pd.DataFrame(data=hourly_data)
        # Formatear la columna 'event_date'
        hourly_dataframe['date'] = pd.to_datetime(hourly_dataframe['date'])  # Convertir a tipo datetime
        hourly_dataframe['Fecha'] = hourly_dataframe['date'].dt.strftime('%Y-%m-%d')  # Extraer la fecha
        hourly_dataframe['Hora'] = hourly_dataframe['date'].dt.strftime('%H')  # Extraer la hora
        hourly_dataframe['Hora'] = hourly_dataframe['Hora'].astype(int)  # Convertir la hora a entero
        
        # Eliminar el componente de la zona horaria UTC
        hourly_dataframe['date'] = hourly_dataframe['date'].dt.tz_localize(None)
        
        # Eliminar la columna original 'event_date'
        hourly_dataframe.drop(columns=['date'], inplace=True)
    
        hourly_dataframe[['Fecha', 'Hora', 'temperature_2m']]  # Reordenar las columnas si es necesario

        # Guardar los datos procesados en un archivo Parquet si no existe
        output_folder = Path('C:\\Users\\ozi\\ti\\MVP_ML_TransporteNY\\datasets\\processed\\data_analytics')
        output_folder.mkdir(parents=True, exist_ok=True)
        output_file = output_folder / 'temperature.parquet'

        if not os.path.exists(output_file):
            hourly_dataframe.to_parquet(output_file, index=False)
            print("Datos meteorológicos procesados y almacenados en:", output_file)
        else:
            print("El archivo ya existe en la ruta especificada. No se volverá a procesar.")

        return hourly_dataframe

# Definir las coordenadas de la ciudad de Nueva York
latitude_nyc = 40.7128
longitude_nyc = -74.0060   

# Especificar el período de tiempo deseado
start_date = "2022-01-01"
end_date = "2023-12-31"

# Especificar las variables meteorológicas que deseas obtener
weather_variables = "temperature_2m"

# Crear una instancia del procesador de datos meteorológicos
processor = WeatherDataProcessor(latitude_nyc, longitude_nyc, start_date, end_date, weather_variables)

# Obtener los datos meteorológicos
responses = processor.fetch_weather_data()

# Procesar los datos meteorológicos
processor.process_weather_data(responses)




class AirQualityProcessor:
    def __init__(self, output_folder):
        self.output_folder = output_folder
    
    def obtener_datos(self):
        """
        Función para obtener los datos de la API Socrata.
        """
        # Unauthenticated client only works with public data sets. Note 'None'
        # in place of application token, and no username or password:
        client = Socrata("data.cityofnewyork.us", None)

        # Example authenticated client (needed for non-public datasets):
        # client = Socrata(data.cityofnewyork.us,
        #                  MyAppToken,
        #                  username="user@example.com",
        #                  password="AFakePassword")

        # First 2000 results, returned as JSON from API / converted to Python list of
        # dictionaries by sodapy.
        results = client.get("c3uy-2p5r", limit=16218)
        
        return results

    def procesar_datos_etl(self, datos):
        """
        Función para realizar el procesamiento ETL (Extract, Transform, Load) a partir de los datos obtenidos.
        """
        # Seleccionar las variables relevantes
        variables_seleccionadas = [
            'geo_place_name', 'geo_type_name', 'start_date',  # Variables de ubicación y tiempo
            'indicator_id', 'name', 'measure', 'measure_info',  # Variables relacionadas con el tráfico
            'data_value',  # Variable de valor de los datos
            'unique_id', 'geo_join_id'  # Variables de identificación
        ]

        # Convertir a pandas DataFrame
        df_tratado = pd.DataFrame.from_records(datos)
        
        # Seleccionar las columnas relevantes del DataFrame
        df_tratado = df_tratado[variables_seleccionadas].copy()

        # Convertir las columnas de fecha y hora a tipos de datos datetime
        df_tratado['start_date'] = pd.to_datetime(df_tratado['start_date'])

        # Convertir la columna 'data_value' a tipo numérico si es posible
        df_tratado['data_value'] = pd.to_numeric(df_tratado['data_value'], errors='coerce')

        # Manejar los valores nulos o valores no numéricos en 'data_value'
        # Por ejemplo, podrías optar por eliminar las filas con valores nulos en 'data_value'
        df_tratado = df_tratado.dropna(subset=['data_value'])
        
        return df_tratado
    
    def guardar_datos(self, df_tratado):
        """
        Función para guardar los datos procesados en un archivo Parquet en la ruta especificada.
        """
        # Crear el directorio de salida si no existe
        output_folder = Path(self.output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)
        
        # Definir el nombre del archivo de salida
        output_file = output_folder / 'air_quality.parquet'

        # Guardar los datos en formato Parquet
        df_tratado.to_parquet(output_file, index=False)
        print(f"Los datos han sido guardados en: {output_file}")

if __name__ == "__main__":
    output_folder = r"C:\Users\ozi\ti\MVP_ML_TransporteNY\datasets\processed\data_analytics"
    
    procesador = AirQualityProcessor(output_folder)
    datos = procesador.obtener_datos()
    df_tratado = procesador.procesar_datos_etl(datos)
    procesador.guardar_datos(df_tratado)


class CKANDataExtractor:
    def __init__(self, ckan_url):
        self.rc = RemoteCKAN(ckan_url)
        self.common_fields = [
            "Model year", "Make", "Model", "Vehicle class", "Engine size (L)",
            "Cylinders", "Transmission", "Fuel type", "City (L/100 km)",
            "Highway (L/100 km)", "Combined (L/100 km)", "Combined (mpg)",
            "CO2 emissions (g/km)", "CO2 rating", "Smog rating"
        ]

    def fetch_data(self, resource_id, limit):
        query = {
            "resource_id": resource_id,
            "fields": self.common_fields,
            "limit": limit
        }
        result = self.rc.action.datastore_search(**query)
        records = result['records']
        df = pd.DataFrame(records)
        return df


class DataCleaner:
    @staticmethod
    def clean_column_names(df):
        df.columns = [DataCleaner.clean_column_name(col) for col in df.columns]
        return df

    @staticmethod
    def clean_column_name(name):
        name = re.sub(r'\W+$', '', str(name))
        name = re.sub(r'\W+', '_', name)
        name = unidecode(name)
        name = name.lower()
        return name

    @staticmethod
    def replace_na_with_zero(df, columns):
        for col in columns:
            df[col] = df[col].replace(['n_a', 'n/a'], 0, regex=True).astype(int)
        return df

    @staticmethod
    def convert_columns_to_int(df, columns):
        for col in columns:
            df[col] = df[col].astype(int)
        return df


class ETLProcessor:
    def __init__(self, ckan_url, output_folder):
        self.ckan_extractor = CKANDataExtractor(ckan_url)
        self.output_folder = output_folder

    def extract_data(self, resource_id, limit):
        return self.ckan_extractor.fetch_data(resource_id, limit)

    def clean_data(self, df):
        df = DataCleaner.clean_column_names(df)
        df = DataCleaner.replace_na_with_zero(df, ['co2_rating', 'smog_rating'])
        df = DataCleaner.convert_columns_to_int(df, ['combined_mpg', 'co2_emissions_g_km', 'model_year', 'cylinders'])
        return df

    def save_data(self, df, filename):
        output_file = Path(self.output_folder) / filename
        df.to_parquet(output_file, index=False)


class CKANDataElectric:
    def __init__(self, ckan_url):
        self.ckan_url = ckan_url
        self.rc = RemoteCKAN(ckan_url)

    def scrape_data(self, resource_id, limit):
        query = {
            "resource_id": resource_id,
            "fields": [
                "Model year",
                "Make",
                "Model",
                "Vehicle class",
                "Motor (kW)",
                "Transmission",
                "Fuel type",
                "City (kWh/100 km)",
                "Highway (kWh/100 km)",
                "Combined (kWh/100 km)",
                "City (Le/100 km)",
                "Highway (Le/100 km)",
                "Combined (Le/100 km)",
                "Range (km)",
                "CO2 emissions (g/km)",
                "CO2 rating",
                "Smog rating",
                "Recharge time (h)"
            ],
            "limit": limit
        }
        result = self.rc.action.datastore_search(**query)
        records = result['records']
        df = pd.DataFrame(records)
        return df

    @staticmethod
    def clean_column_names(column_name):
        """
        Clean and format column names.

        Parameters:
        - column_name (str): The name of the column to clean.

        Returns:
        str: The cleaned and formatted column name.
        """
        column_name = re.sub(r'\W+$', '', str(column_name))  # Remove any trailing underscore
        column_name = re.sub(r'\W+', '_', column_name)  # Replace other non-alphanumeric characters with underscores
        column_name = unidecode(column_name)
        column_name = column_name.lower()
        return column_name

    def clean_data(self, df):
        """
        Apply data cleaning and formatting to the DataFrame.

        Parameters:
        - df (DataFrame): The DataFrame to clean and format.

        Returns:
        DataFrame: The cleaned and formatted DataFrame.
        """
        # Apply cleaning and formatting to all cells of the DataFrame
        df_cleaned = df.applymap(lambda x: self.clean_column_names(x) if isinstance(x, str) else x)

        # Rename the columns of the DataFrame with cleaned and formatted names
        df_cleaned.columns = [self.clean_column_names(col) for col in df_cleaned.columns]

        # Convert 'model_year' column to integer
        df_cleaned['model_year'] = df_cleaned['model_year'].astype(int)

        # Convert 'co2_emissions_g_km' column to integer
        df_cleaned['co2_emissions_g_km'] = df_cleaned['co2_emissions_g_km'].astype(int)

        # Replace 'n_a' or 'n/a' with 0 and convert 'co2_rating' column to integer
        df_cleaned['co2_rating'] = df_cleaned['co2_rating'].replace(['n_a', 'n/a'], 0, regex=True).astype(int)

        # Replace 'n_a' or 'n/a' with 0 and convert 'smog_rating' column to integer
        df_cleaned['smog_rating'] = df_cleaned['smog_rating'].replace(['n_a', 'n/a'], 0, regex=True).astype(int)

        return df_cleaned

    def save_data(self, df, output_folder):
        """
        Save the cleaned and formatted DataFrame to a Parquet file.

        Parameters:
        - df (DataFrame): The cleaned and formatted DataFrame to save.
        - output_folder (str): The path to the output folder where the Parquet file will be saved.
        """
        output_file = output_folder + '/electric_consumption.parquet'
        df.to_parquet(output_file, index=False)
        print("Data saved successfully.")

if __name__ == "__main__":
    ckan_url = 'https://open.canada.ca/data/en/'
    output_folder = r"C:\Users\ozi\ti\MVP_ML_TransporteNY\datasets\processed\data_analytics"

    etl_processor = ETLProcessor(ckan_url, output_folder)

    resources = [
        ("42495676-28b7-40f3-b0e0-3d7fe005ca56", 7292),
        ("2309538b-53d1-4635-a88e-e237bfcef7a2", 10562),
        ("332be680-9577-42c6-8c47-a0380ef48c5e", 5432),
        ("56a89c09-d609-41cd-8838-9dd9905d3cfc", 975),
        ("f2e53a2b-e075-473a-9a9c-5d7bef68d07d", 971),
        ("87fc1b5e-fafc-4d44-ac52-66656fc2a245", 971),
        ("b6100f60-5e63-437d-b122-db76c467c0a7", 833),
        ("edba4afa-dc19-480c-bbe4-57992fc9d0d6", 833),
    ]

    for i, (resource_id, limit) in enumerate(resources, start=1):
        df = etl_processor.extract_data(resource_id, limit)
        df = etl_processor.clean_data(df)
        filename = f"fuel_consumption_{i}.parquet"
        etl_processor.save_data(df, filename)

    # Instanciar la clase CKANDataElectric
    ckan_processor = CKANDataElectric(ckan_url='https://open.canada.ca/data/en/')

    # Scraping de datos desde CKAN
    df_electric = ckan_processor.scrape_data(resource_id="026e45b4-eb63-451f-b34f-d9308ea3a3d9", limit=668)

    # Limpiar y formatear los datos
    df_cleaned = ckan_processor.clean_data(df_electric)

    # Guardar los datos limpios en formato Parquet
    #output_folder = r"C:\Users\ozi\ti\MVP_ML_TransporteNY\datasets\processed\data_analytics"
    ckan_processor.save_data(df_cleaned, output_folder)
