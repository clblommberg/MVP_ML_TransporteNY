import pandas as pd
from pathlib import Path
import pandas as pd
import zipfile


class DataProcessor:
    def __init__(self, input_file, output_folder):
        self.input_file = input_file
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def process_and_save(self):
        # Leer el archivo CSV en un DataFrame
        df = pd.read_csv(self.input_file)

        # Eliminar la columna 'service_zone'
        df.drop(columns=['service_zone'], inplace=True)

        # Guardar el DataFrame procesado en formato Parquet
        output_file = self.output_folder / 'service_zone.parquet'
        df.to_parquet(output_file, index=False)

        print("Data processing complete. Saved to:", output_file)

class DataExtractor:
    def __init__(self, zip_file, output_folder):
        self.zip_file = zip_file
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def extract_and_process(self):
        # Lista para almacenar los datos de los archivos CSV
        datos_csv = []

        # Abrir el archivo zip y leer los csv
        with zipfile.ZipFile(self.zip_file, 'r') as zip_ref:
            # Recorrer cada archivo en el zip
            for nombre_archivo in zip_ref.namelist():
                # Extraer archivo
                with zip_ref.open(nombre_archivo) as archivo_csv:
                    # Leer csv y almacenar datos en un df
                    datos = pd.read_csv(archivo_csv, sep=',', encoding='utf-8')
                    # Agregar los datos a la lista
                    datos_csv.append(datos)

        # Concatenar todos los df en uno solo
        df_emisiones = pd.concat(datos_csv, ignore_index=True)

        # Filtrar por país 'United States'
        df_emisiones_usa = df_emisiones[df_emisiones['Country'] == 'United States']

        # Filtrar por tipos de energía: 'petroleum_n_other_liquids' y 'renewables_n_other'
        emisiones_usa = df_emisiones_usa.loc[(df_emisiones_usa['Energy_type'] == 'petroleum_n_other_liquids') | (df_emisiones_usa['Energy_type'] == 'renewables_n_other')]

        # Eliminar columnas no deseadas
        columns_to_drop = ['Unnamed: 0', 'Country', 'Energy_intensity_per_capita', 'Energy_intensity_by_GDP']
        emisiones_usa.drop(columns=columns_to_drop, inplace=True)

        # Renombrar columnas
        new_column_names = {
            'Energy_type': 'TipoEnergia',
            'Year': 'Anio',
            'Energy_consumption': 'ConsumoEnergia',
            'Energy_production': 'ProducionEnergia',
            'GDP': 'ConsumoPerCapita',
            'Population': 'Poblacion',
            'CO2_emission': 'CantidadEmisionesCO2'
        }
        emisiones_usa.rename(columns=new_column_names, inplace=True)

        # Reordenar las columnas del DataFrame
        new_column_order = ['Anio', 'TipoEnergia', 'ProducionEnergia', 'ConsumoEnergia', 'Poblacion', 'ConsumoPerCapita', 'CantidadEmisionesCO2']
        emisiones_usa = emisiones_usa.reindex(columns=new_column_order)

        # Guardar el DataFrame procesado en formato Parquet
        output_file = self.output_folder / 'emisiones_usa.parquet'
        emisiones_usa.to_parquet(output_file, index=False)

        print("Data extraction and processing complete. Saved to:", output_file)


if __name__ == "__main__":
    # Ruta al archivo CSV de entrada
    input_file = "..\\datasets\\raw\\taxi_zone_lookup.csv"   
    # Ruta a la carpeta de salida para el archivo Parquet
    output_folder = "..\\datasets\\processed\\data_analytics"
    
    # Crear una instancia de la clase DataProcessor y procesar los datos
    processor = DataProcessor(input_file, output_folder)
    processor.process_and_save()


    # Ruta al archivo ZIP de entrada
    ruta_zip = '..\\datasets\\raw\\archive.zip'
    # Ruta a la carpeta de salida para el archivo Parquet
    output_folder_a = "..\\datasets\\processed\\data_analytics"

    # Crear una instancia de la clase DataExtractor y extraer los datos
    extractor = DataExtractor(ruta_zip, output_folder_a)
    extractor.extract_and_process()