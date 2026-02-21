from src.ml_deployment import logger

# logger.info('Wellcom to custom logging')
from src.ml_deployment.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME='Data ingestion stage'

try:
    logger.info(f'>>>>>>>>>stage {STAGE_NAME} STARTED')
    
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>. stage {STAGE_NAME} completed <<<<<\n\nx======x')
    
except Exception as e:
    logger.exception(e)
    raise e