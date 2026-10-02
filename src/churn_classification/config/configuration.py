import os
from src.churn_classification.constants import *
from src.churn_classification.utils.common import read_yaml, create_directories
from pydantic import validate_call
from src.churn_classification.entity.config_entity import (DataIngestionConfig,
                                                           DataValidationConfig,
                                                           DataTransformationConfig
                                                           )

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
        self.schema=read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])

                
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config
        create_directories([config.data_ingestion.root_dir])
        return DataIngestionConfig(**self.config.data_ingestion)
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config
        schema = self.schema.COLUMNS
        create_directories([config.data_validation.root_dir])
        return DataValidationConfig(**self.config.data_validation, all_schema=schema)

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config
        target_column = self.schema.TARGET_COLUMN
        create_directories([config.data_transformation.root_dir])
        return DataTransformationConfig(**self.config.data_transformation, target_column=target_column)










