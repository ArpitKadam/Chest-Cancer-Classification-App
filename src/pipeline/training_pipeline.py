from src.logger import logger
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.base_model import PrepareBaseModel
from src.components.model_trainer import ModelTrainer
from src.configuration.configuration import AppConfig
import sys
import datetime

class Train:
    def __init__(self):
        self.c = 0
        self.line = "*"*30
        print(f"{self.line}>  Initiated {self.c}  <{self.line}")
    
    def train(self):
        try:
            self.c += 1
            print(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} - Starting Data Ingestion Pipeline  {self.line}>")
            logger.info(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} - Starting Data Ingestion Pipeline  {self.line}>")
            config = AppConfig()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion_obj = DataIngestion(config=data_ingestion_config)
            data_ingestion_obj.download_data()
            data_ingestion_obj.unzip_data()
            print(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} -  Data Ingestion Pipeline Completed  {self.line}>")
            logger.info(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} - Data Ingestion Pipeline Completed  {self.line}>")

            self.c += 1
            print(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} -  Starting Base Model Preparation  {self.line}>")
            logger.info(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} -  Starting Base Model Preparation  {self.line}>")
            config = AppConfig()
            prepare_base_model = config.get_base_model_config()
            prepare_base_model =  PrepareBaseModel(config=prepare_base_model)
            prepare_base_model.download_base_mode()
            prepare_base_model.update_base_model()
            print(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} -  Base Model Preparation Completed  {self.line}>")
            logger.info(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} -  Base Model Preparation Completed  {self.line}>")

            self.c += 1
            print(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} -  Starting Model Training  {self.line}>")
            logger.info(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} -  Starting Model Training  {self.line}>")
            config = AppConfig()
            trainer_config = config.get_model_trainer_config()
            training = ModelTrainer(config=trainer_config)
            training.get_model()
            training.get_data_for_training()
            training.train()
            training.save_training_metrics()
            print(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} -  Model Training Completed  {self.line}>")
            logger.info(f"{self.line}>  [{datetime.datetime.now()}] -  Stage {self.c} -  Model Training Completed  {self.line}>")

        except Exception as e:
            raise CustomException(e, sys)