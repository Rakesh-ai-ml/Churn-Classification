from src.churn_classification.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.churn_classification.logger import logger


STAGE_NAME = "Data Ingestion stage"

try:
   logger.info(f"---------------->> stage {STAGE_NAME} started <<----------------") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.initiate_data_ingestion()
   logger.info(f"---------------->> stage {STAGE_NAME} completed <<----------------\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

