from pathlib import Path
from pydantic import BaseModel
from typing import List

class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_PATH: str
    local_data_file: Path
    unzip_dir: Path

class DataValidationConfig(BaseModel):
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: List[str]

class DataTransformationConfig(BaseModel):
    root_dir: Path
    data_path: Path
    train_data_file: Path
    test_data_file: Path
    target_column: str
