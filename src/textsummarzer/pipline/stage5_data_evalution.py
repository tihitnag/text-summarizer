from textsummarizer.components.data_evaluation import ModelEvaluation
from  textsummarzer.config.configuration import ConfigurationManager
 
 
class model_evaluation_pipline:
    def __init__(self,config=ModelEvaluation):
        pass
    def main(self):
        
        
        config=ConfigurationManager()
        DataEvalConfig=config.get_model_evaluation_config()
        DataTrainConfig=ModelEvaluation(config=DataEvalConfig)
        DataTrainConfig.evaluate()