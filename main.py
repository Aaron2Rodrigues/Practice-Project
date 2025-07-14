from src.Salary_project import logger
from src.Salary_project.pipeline.DataIngestionPipeline  import DataIngestionTrainigPipeline

Stage_name = 'Data Ingestion Pipeline'

try:
    logger.info(f'>>>>>>>>> {Stage_name} started <<<<<<<<<')
    data_ingestion = DataIngestionTrainigPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f'>>>>>>>>> {Stage_name} completed <<<<<<<<\n\nx======x')
except Exception as e:
    logger.exception(e)
    raise e

