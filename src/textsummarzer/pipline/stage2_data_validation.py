#create the pipline
from textsummarzer.config.configuration import ConfigurationManager
from textsummarzer.components.data_validation import DataValidation
#from textsummarzer.logging import Logger

class Validation_pipline():
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        DataValidationConfig=config.get_data_validation_config()
        data_validation=DataValidation(config=DataValidationConfig)
        data_validation.validation_all_files()
