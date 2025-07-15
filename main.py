from src.Salary_project import logger
from src.Salary_project.pipeline.DataIngestionPipeline  import DataIngestionTrainigPipeline
from src.Salary_project.pipeline.DataValidationPipeline import DataValidationPipeline

Stage_name = 'Data Ingestion Pipeline'

try:
    logger.info(f'>>>>>>>>> {Stage_name} started <<<<<<<<<')
    data_ingestion = DataIngestionTrainigPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f'>>>>>>>>> {Stage_name} completed <<<<<<<<\n\nx======x')
except Exception as e:
    logger.exception(e)
    raise e

Stage_name = 'Data Validation Pipeline'

try:
    logger.info(f'>>>>>>>>> {Stage_name} started <<<<<<<<<')
    data_validation = DataValidationPipeline()
    data_validation.initiate_data_validation()
    logger.info(f'>>>>>>>>> {Stage_name} completed <<<<<<<<<\n\nx=====x')
except Exception as e:
    logger.exception(e)
    raise e