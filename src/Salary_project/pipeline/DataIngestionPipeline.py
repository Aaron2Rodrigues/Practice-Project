from src.Salary_project.config.configuration import ConfigurationManager
from src.Salary_project.components.data_ingestion import DataIngestion
from src.Salary_project import logger

class DataIngestionTrainigPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigurationManger()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()