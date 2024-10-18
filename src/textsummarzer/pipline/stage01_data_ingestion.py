#create the pipline
from textsummarzer.config.configuration import ConfigurationManager
from textsummarzer.components.data_ingestion import Data_Ingestion
#from textsummarzer.logging import Logger

class DataIngestion_pipline:
    def __init__(self):
        pass
    def main(self):
    
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=Data_Ingestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
