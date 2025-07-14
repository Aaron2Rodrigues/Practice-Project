from src.Salary_project.entity.config_entity import DataIngestionConfig
from src.Salary_project import logger
from src.Salary_project.utils.common import read_yaml,create_directories
from src.Salary_project.constants import *

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH,schema_filepath=SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifact_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.DataIngestion
        create_directories([self.config.DataIngestion.root_dir])
    

        data_ingestion = DataIngestionConfig(
            root_dir = config.root_dir,
            input_path = config.input_path,
            output_path = config.output_path
        )
        return data_ingestion