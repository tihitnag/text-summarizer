import os
import urllib.request as request
import zipfile
from pathlib import Path
from textsummarzer.logging import logger
from textsummarzer.utils.common import get_size
from textsummarzer.entity import DataIngestionconfig
class Data_Ingestion:
    def __init__(self, config: DataIngestionconfig):
        self.config = config

    
    def download_file(self):
        if not os.path.exists(self.config.local_data_files):
            filename, headers = request.urlretrieve(
                url = self.config.source_urls,
                filename = self.config.local_data_files
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_files))}")  

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_files, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)