from chicken_disease import logger
from chicken_disease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chicken_disease.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"****************")
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main() 
    logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e