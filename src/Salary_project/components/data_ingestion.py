from src.Salary_project.config.configuration import ConfigurationManager
from src.Salary_project.entity.config_entity import DataIngestionConfig
from src.Salary_project import logger
import pandas as pd

class Dataingestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def load_file(self):
        data = pd.read_csv(self.config.input_path)
        data = data.to_csv(self.config.output_path)
        return data
   