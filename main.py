# pipeline execution
from textsummarzer.logging import logger
from textsummarzer.pipline.stage01_data_ingestion import DataIngestion_pipline
from textsummarzer.pipline.stage2_data_validation import Validation_pipline
from textsummarzer.pipline.stage3_data_transformation import data_transformation_pipline
stage_name = 'data ingestion stage'
try:
    logger.info(f'>> Stage {stage_name} started')
    
    data_ingestion = DataIngestion_pipline()
    data_ingestion.main()
    
    logger.info(f'>> Stage {stage_name} completed')
except Exception as e:
    logger.exception(e)
    raise e


try:
    data_val=Validation_pipline()
    data_val.main()
    logger.info (f'>> Data validation completed')
except Exception as e:
    logger.exception(e)
    raise e
try:
    data_trans=data_transformation_pipline()
    data_val.main()
    logger.info (f'>> Data validation completed')
except Exception as e:
    logger.exception(e)
    raise e