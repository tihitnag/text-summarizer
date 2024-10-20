from textsummarzer.components.data_trainer import ModelTrainer
from textsummarzer.config.configuration import ConfigurationManager

class data_trainer_pipline():
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        DataTrainConfig=config.get_data_trainer_config()
        DataTrainConfig=ModelTrainer(config=DataTrainConfig)
        DataTrainConfig.train()

