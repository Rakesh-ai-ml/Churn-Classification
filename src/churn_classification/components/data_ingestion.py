import os
from src.churn_classification.logger import logger
import zipfile
from src.churn_classification.entity.config_entity import (DataIngestionConfig)
from dotenv import load_dotenv
load_dotenv()
import subprocess
import kaggle

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    def download_file(self):
        # Use Kaggle CLI to download dataset
        cmd = [
            "kaggle", "datasets", "download",
            "-d", self.config.source_PATH,
            "-p", str(self.config.root_dir),
            "--force"
        ]

        if not os.path.exists(self.config.local_data_file):

            subprocess.run(cmd, check=True)
            logger.info(f" Data file download successful")

        else:
            logger.info(f"File already exists")



    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f" Data file unzip successful")


