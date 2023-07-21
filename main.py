from cnnClassifier import logger
from cnnClassifier.pipeline.stage01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage03_train import ModelTrainingPipeline
from cnnClassifier.pipeline.stage04_evaluation import EvaluationPipeline
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

if __name__ == "__main__":
    try:
        logger.info(f"********************************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        prepare_base_model=PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<< \n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Training"

try:
    logger.info(f"********************************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME="Evaluation stage"

if __name__ == "__main__":
    try:
        logger.info(f"********************************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} Completed <<<<<< \n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e