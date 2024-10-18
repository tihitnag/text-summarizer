import os
import urllib.request as request
from textsummarzer.logging import logger
from textsummarzer.entity import DataValidationConfig

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config
    def validation_all_files(self)->bool:
        #we can check the data typea and column type
        # check and write the validation status to the status file
          #checking the validation staus file existence
        try:
          
            validation_status=None
            all_files=os.listdir(os.path.join('artifacts','data_ingestion','samsum_dataset'))
            for file in all_files:
                if file not in self.config.required_file:
                    validation_status=False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"validaiton status: {validation_status}")
                else:
                    validation_status=True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f"validaiton status: {validation_status}")
                        
            return  validation_status
        except Exception as e:
            raise e