from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e