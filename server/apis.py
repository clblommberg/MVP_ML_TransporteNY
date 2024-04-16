import openmeteo_requests
import requests_cache
from retry_requests import retry
import pandas as pd
from pathlib import Path
import os

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

        # Guardar los datos procesados en un archivo Parquet si no existe
        output_folder = Path('..\\datasets\\processed\\data_analytics')  # Cambio de ruta de salida
        output_folder.mkdir(parents=True, exist_ok=True)
        output_file = output_folder / 'temperature.parquet'

        if not os.path.exists(output_file):
            hourly_dataframe.to_parquet(output_file, index=False)
            print("Datos meteorológicos procesados y almacenados.")
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
