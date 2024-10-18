from textsummarzer.components.data_transformation import DataTransforamtion
from textsummarzer.config.configuration import ConfigurationManager

class data_transformation_pipline():
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        DataTransformationConfig=config.get_data_transformation_config()
        data_validation=DataTransforamtion(config=DataTransformationConfig)
        data_validation.convert()