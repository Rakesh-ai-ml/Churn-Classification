import os
from src.churn_classification.constants import *
from src.churn_classification.utils.common import read_yaml, create_directories
from src.churn_classification.entity.config_entity import DataIngestionConfig
from pydantic import validate_call
# from src.churn_classification.entity.config_entity import DataIngestionConfig  
from src.churn_classification.constants.constants import (
                                                            CONFIG_FILE_PATH,
                                                            PARAMS_FILE_PATH,
                                                            SCHEMA_FILE_PATH
                                                        )


class ConfigurationManager:

    def __init__(
                self,
                config_filepath=CONFIG_FILE_PATH,
                params_filepath = PARAMS_FILE_PATH,
                schema_filepath = SCHEMA_FILE_PATH
                ):
        
        self.config=read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])

                
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config
        create_directories([config.data_ingestion.root_dir])
        return DataIngestionConfig(**self.config.data_ingestion)
    











