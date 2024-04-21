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
        datos_csv = []

        with zipfile.ZipFile(self.zip_file, 'r') as zip_ref:
            for nombre_archivo in zip_ref.namelist():
                with zip_ref.open(nombre_archivo) as archivo_csv:
                    datos = pd.read_csv(archivo_csv, sep=',', encoding='utf-8')
                    datos_csv.append(datos)

        df_emisiones = pd.concat(datos_csv, ignore_index=True)

        df_emisiones_usa = df_emisiones[df_emisiones['Country'] == 'United States']

        emisiones_usa = df_emisiones_usa.loc[(df_emisiones_usa['Energy_type'] == 'petroleum_n_other_liquids') | (df_emisiones_usa['Energy_type'] == 'renewables_n_other')].copy()

        columns_to_drop = ['Unnamed: 0', 'Country', 'Energy_intensity_by_GDP','GDP']
        emisiones_usa.drop(columns=columns_to_drop, inplace=True)

        new_column_names = {
            'Energy_type': 'TipoEnergia',
            'Year': 'Anio',
            'Energy_consumption': 'ConsumoEnergia',
            'Energy_production': 'ProducionEnergia',
            'Energy_intensity_per_capita': 'ConsumoPerCapita',
            'Population': 'Poblacion',
            'CO2_emission': 'CantidadEmisionesCO2'
        }
        emisiones_usa.rename(columns=new_column_names, inplace=True)

        new_column_order = ['Anio', 'TipoEnergia', 'ProducionEnergia', 'ConsumoEnergia', 'Poblacion', 'ConsumoPerCapita', 'CantidadEmisionesCO2']
        emisiones_usa = emisiones_usa.reindex(columns=new_column_order)

        output_file = self.output_folder / 'emisiones_usa.parquet'
        emisiones_usa.to_parquet(output_file, index=False)

        print("Data extraction and processing complete. Saved to:", output_file)


class AcousticDataProcessor:
    def __init__(self, input_file, output_folder):
        self.input_file = input_file
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def process_data(self):
        df = pd.read_csv(self.input_file)

        variables_seleccionadas = ['latitude', 'longitude', 'year', 'hour', '1-3_large-sounding-engine_presence', 
                                   '1_engine_presence', '7_human-voice_presence', '2_machinery-impact_presence', 
                                   '4_powered-saw_presence', '5_alert-signal_presence', '6_music_presence', 
                                   'sensor_id', 'annotator_id']
        df_procesado = df[variables_seleccionadas].copy()

        # Verificar si 'audio_filename' está presente en el DataFrame antes de realizar modificaciones
        if 'audio_filename' in df_procesado.columns:
            df_procesado['audio_filename'] = df_procesado['audio_filename'].str.replace('.wav', '')
            df_procesado['audio_filename_code'] = pd.Categorical(df_procesado['audio_filename']).codes
        else:
            print("La columna 'audio_filename' no está presente en el DataFrame.")

        return df_procesado

    def save_processed_data(self, df):
        output_file = self.output_folder / 'acustic_usa.parquet'
        df.to_parquet(output_file, index=False)
        print("Acoustic data processing complete. Saved to:", output_file)


if __name__ == "__main__":
    input_file = "..\\datasets\\raw\\taxi_zone_lookup.csv"   
    output_folder = "..\\datasets\\processed\\data_analytics"
    
    processor = DataProcessor(input_file, output_folder)
    processor.process_and_save()

    ruta_zip = '..\\datasets\\raw\\archive.zip'
    output_folder_a = "..\\datasets\\processed\\data_analytics"

    extractor = DataExtractor(ruta_zip, output_folder_a)
    extractor.extract_and_process()

    input_file_a = "..\\datasets\\raw\\datos.csv"   
    output_folder_a = "..\\datasets\\processed\\data_analytics"

    acoustic_processor = AcousticDataProcessor(input_file_a, output_folder_a)
    acoustic_data = acoustic_processor.process_data()
    acoustic_processor.save_processed_data(acoustic_data)
