from src.logger import logger
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.configuration.configuration import AppConfig
import sys
import datetime

class Train:
    def __init__(self):
        self.c = 0
        print(f"============>  Initiated {self.c}  <============")
    
    def train(self):
        try:
            self.c += 1
            print(f"============>  [{datetime.datetime.now()}] -  Stage {self.c} - Starting Data Ingestion Pipeline  <============")
            logger.info(f"============>  [{datetime.datetime.now()}] -  Stage {self.c} - Starting Data Ingestion Pipeline  <============")
            config = AppConfig()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion_obj = DataIngestion(config=data_ingestion_config)
            data_ingestion_obj.download_data()
            data_ingestion_obj.unzip_data()
            print(f"============>  [{datetime.datetime.now()}] -  Stage {self.c} -  Data Ingestion Pipeline Completed  <============")
            logger.info(f"============>  [{datetime.datetime.now()}] -  Stage {self.c} - Data Ingestion Pipeline Completed  <============")
        except Exception as e:
            raise CustomException(e, sys)