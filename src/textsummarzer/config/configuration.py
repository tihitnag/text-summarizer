from textsummarzer.constants import *
from textsummarzer.utils.common import read_yaml,create_directory
from textsummarzer.entity import DataIngestionconfig
from textsummarzer.entity import DataValidationConfig
from textsummarzer.entity import DataTransforamtionConfig
class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        
        create_directory([self.config.artifacts_root]) 
    def get_data_ingestion_config(self)->DataIngestionconfig:
      
      config=self.config.data_ingestion
      create_directory([config.root_dir])
      data_ingestion_config=DataIngestionconfig(
      root_dir=config.root_dir ,
      source_urls=config.source_urls,
      local_data_files=config.local_data_files , #Path(config.local_data_files)
      unzip_dir=config.unzip_dir  #Path(config.unzip_dir)
      )
      return data_ingestion_config
    def get_data_validation_config(self)->DataValidationConfig:
      
      config=self.config.data_validation
      create_directory([config.root_dir])
      
      data_validation_config=DataValidationConfig(
      root_dir=config.root_dir ,
      status_file=config.status_file,
      required_file=config.required_file,  )
      
      return data_validation_config
  
    def get_data_transformation_config(self)->DataTransforamtionConfig:
      
      config=self.config.data_transformation
      create_directory([config.root_dir])
      
      data_transformation_config=DataTransforamtionConfig(
        root_dir=config.root_dir ,
         data_path= config.data_path,
         tokenizer_name=config.tokenizer_name,
      )
      
      return data_transformation_config