from src.Salary_project.components.data_validation import DataValidation
from src.Salary_project.config.configuration import ConfigurationManager
from src.Salary_project import logger

class DataValidationPipeline:

    def __init__(self):
        pass

    def initiate_data_validation (self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()
        