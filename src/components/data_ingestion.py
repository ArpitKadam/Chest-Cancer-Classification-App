from src.logger import logger
from src.exception import CustomException
import gdown
import os, sys
import zipfile
from src.configuration.configuration import AppConfig
from src.entity.config_entity import DataIngestionConfig
from src.utils import create_directories

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self) -> str:
        try:
            root_dir = self.config.root_dir
            data_url = self.config.source_url
            zip_download_dir = self.config.data_dir

            create_directories([root_dir])            ### Now always pass path to this function as list
            logger.info(f"Data Ingestion directory created at {root_dir}")

            gdown.download(data_url, zip_download_dir)
            logger.info(f"Data downloaded from {data_url} and saved at {zip_download_dir}")

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
    
    def unzip_data(self):
        try:
            unzip_dir = self.config.unzip_dir
            zip_download_dir = self.config.data_dir

            create_directories([unzip_dir])             ### Now always pass path to this function as list
            logger.info(f"Unzip directory created at {unzip_dir}")

            with zipfile.ZipFile(zip_download_dir, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
            
            logger.info(f"Data unzipped from {zip_download_dir} and saved at {unzip_dir}")

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)