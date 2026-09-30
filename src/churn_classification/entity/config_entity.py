from pathlib import Path
from pydantic import BaseModel

class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_PATH: str
    local_data_file: Path
    unzip_dir: Path