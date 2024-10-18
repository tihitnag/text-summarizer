# pipeline execution
from textsummarzer.logging import logger
from textsummarzer.pipline.stage1_data_ingestion import DataIngestion_pipline

stage_name = 'data ingestion stage'
try:
    logger.info(f'>> Stage {stage_name} started')
    
    data_ingestion = DataIngestion_pipline()
    data_ingestion.main()
    
    logger.info(f'>> Stage {stage_name} completed')
except Exception as e:
    logger.exception(e)
    raise e
