from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from pathlib import Path
import requests
from datetime import datetime
import signal
import sys
from urllib.parse import urljoin

class DatasetDownloader:
    def __init__(self, base_url, download_folder):
        self.base_url = base_url
        self.download_folder = Path(download_folder)
        self.download_folder.mkdir(parents=True, exist_ok=True)
        
    def record_start_time(self):
        # Crear una carpeta para controles si no existe
        control_folder = Path('logs') / 'controles'
        control_folder.mkdir(parents=True, exist_ok=True)
        # Crear y registrar la fecha y hora de inicio en un archivo de texto
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(control_folder / 'scrapy_log.txt', 'a') as file:
            file.write(f"Proceso iniciado: {start_time}\n")

    def record_end_time(self):
        # Registrar la fecha y hora de finalización en el mismo archivo de texto
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('logs\\controles\\scrapy_log.txt', 'a') as file:
            file.write(f"Proceso finalizado: {end_time}\n\n")

    def signal_handler(self, signal, frame):
        print("Capturada señal de interrupción. Registrando hora de finalización.")
        self.record_end_time()
        sys.exit(0)

    def scrape_siniestros_urls(self):
        options = Options()
        options.headless = True
        service = Service('geckodriver.exe')  # Ruta al ejecutable de GeckoDriver
        driver = webdriver.Firefox(service=service, options=options)
        driver.get(self.base_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "a")))
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        links = soup.find_all('a')
        file_urls = {}
        for link in links:
            href = link.get('href')
            if href:
                href = href.strip()
                if any(year in href for year in ['2022', '2023']) or 'taxi_zone_lookup' in href or 'taxi_zones' in href:
                    if href.endswith(('.zip', '.xlsx', '.csv', '.gz', '.geojson', '.pdf', '.parquet')):
                        file_name = href.split('/')[-1]
                        if 'green_tripdata' in file_name or 'fhv_tripdata' in file_name:
                            continue  # Saltar archivos green_tripdata y fhv_tripdata
                        file_urls[file_name] = href
        driver.quit()
        return file_urls

    def download_file(self, url, save_path):
        try:
            if not save_path.exists():
                response = requests.get(url, stream=True)
                response.raise_for_status()
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Archivo guardado: {save_path}")
            else:
                print(f"El archivo {save_path} ya existe, no es necesario descargarlo nuevamente.")
        except Exception as e:
            print(f"Error al descargar el archivo: {url}")
            print(f"Error details: {e}")

    def download_datasets(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        self.record_start_time()  # Registrar la hora de inicio
        file_urls_dict = self.scrape_siniestros_urls()
        for file_name, url in file_urls_dict.items():
            save_path = self.download_folder / file_name
            self.download_file(url, save_path)
        self.record_end_time()  # Registrar la hora de finalización

class WebScraper:
    def __init__(self, base_url, download_folder):
        self.base_url = base_url
        self.download_folder = Path(download_folder)
        self.download_folder.mkdir(parents=True, exist_ok=True)

    def scrape_dataset_url(self):
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        dataset_link = soup.find('a', string='README.md')
        if dataset_link:
            absolute_url = urljoin(self.base_url, dataset_link['href'])
            readme_url = absolute_url
        else:
            print("No se encontró el enlace al README.md")
            readme_url = None

        csv_link = soup.select_one('a[href*="annotations.csv"]')
        if csv_link:
            csv_url = urljoin(self.base_url, csv_link['href'])
        else:
            print("No se encontró el enlace al archivo CSV")
            csv_url = None

        return readme_url, csv_url

    def download_file(self, url, save_path):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Archivo guardado: {save_path}")
        except Exception as e:
            print(f"Error al descargar el archivo: {url}")
            print(f"Error details: {e}")

    def download_datasets(self):
        readme_url, csv_url = self.scrape_dataset_url()
        if readme_url:
            save_path = self.download_folder / 'README.md'
            self.download_file(readme_url, save_path)

        if csv_url:
            save_path = self.download_folder / 'datos.csv'
            self.download_file(csv_url, save_path)


if __name__ == "__main__":
    # Uso de ejemplo
    base_url = 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
    download_folder = '..\\datasets\\raw'
    downloader = DatasetDownloader(base_url, download_folder)
    downloader.download_datasets()

    # Uso de ejemplo de la clase DatasetDownloader
    base_url_2 = 'https://zenodo.org/records/3966543'
    download_folder_2 = '../datasets/raw'
    downloader = WebScraper(base_url_2, download_folder_2)
    downloader.download_datasets()
