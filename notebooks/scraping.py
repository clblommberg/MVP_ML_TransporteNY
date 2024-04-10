from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import re


class DatasetDownloader:
    def __init__(self, base_url, download_folder, month):
        self.base_url = base_url
        self.download_folder = Path(download_folder)
        self.month = month
        self.download_folder.mkdir(parents=True, exist_ok=True)


    def scrape_siniestros_urls(self):
        options = Options()
        options.headless = True
        service = Service('/usr/local/bin/geckodriver')  # Ruta al ejecutable de GeckoDriver
        driver = webdriver.Firefox(service=service, options=options)

        driver.get(self.base_url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        links = soup.find_all('a')
        file_urls = {}
        for link in links:
            href = link.get('href')
            if href:
                href = href.strip()
                pattern = r'202\[2-3\]_\d{2}\.parquet$'
                match = re.search(pattern, href)
                if match and f'202{match.group()[-7:-5]}' == self.month:
                    if href.endswith(('.zip', '.xlsx', '.csv', '.gz', '.geojson', '.pdf', '.parquet')):
                        file_name = href.split('/')[-1]
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
        file_urls_dict = self.scrape_siniestros_urls()
        for file_name, url in file_urls_dict.items():
            save_path = self.download_folder / file_name
            self.download_file(url, save_path)

# Uso de ejemplo
base_url = 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page'
download_folder = '../datasets/raw'
month = '01'  # Cambiar a cualquier mes deseado en formato 'MM'
downloader = DatasetDownloader(base_url, download_folder, month)
downloader.download_datasets()
