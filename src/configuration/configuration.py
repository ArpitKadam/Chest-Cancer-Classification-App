from src.logger import logger
from src.exception import CustomException
from src.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.utils import create_directories, read_yaml
from src.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, ModelTrainerConfig
from pathlib import Path
import sys

class AppConfig:
    def __init__(self):
        try:
            self.config_filepath = CONFIG_FILE_PATH
            self.params_filepath = PARAMS_FILE_PATH

            self.config = read_yaml(self.config_filepath)
            logger.info(f"Config file read successfully from {self.config_filepath}")
            self.params = read_yaml(self.params_filepath)
            logger.info(f"Params file read successfully from {self.params_filepath}")

            create_directories([self.config.artifacts_root])   ### Now always pass path to this function as list
            logger.info(f"Artifacts directory created at {self.config.artifacts_root}")

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config = self.config.data_ingestion

            create_directories([config.root_dir])              ### Now always pass path to this function as list
            logger.info(f"Data Ingestion directory created at {config.root_dir}")

            data_ingestion_config = DataIngestionConfig(
                root_dir = config.root_dir,
                source_url = config.source_url,
                data_dir = config.data_dir,
                unzip_dir = config.unzip_dir
            )
            logger.info(f"Data Ingestion Config: {data_ingestion_config}")
            
            return data_ingestion_config

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
    
    def get_base_model_config(self) -> PrepareBaseModelConfig:
        try:
            config = self.config.base_model_preparation
            params = self.params

            create_directories([config.root_dir])            ### Now always pass path to this function as list
            logger.info(f"Base Model directory created at {config.root_dir}")

            base_model_config = PrepareBaseModelConfig(
                root_dir = Path(config.root_dir),
                base_model_path = Path(config.base_model_path),
                updated_base_model_path = Path(config.updated_base_model_path),
                augmentation = params.AUGMENTATION,
                image_size = params.IMAGE_SIZE,
                learning_rate = params.LEARNING_RATE,
                epochs = params.EPOCHS,
                batch_size = params.BATCH_SIZE,
                num_classes = params.CLASSES,
                include_top = params.INCLUDE_TOP,
                weights = params.WEIGHTS
            )
            logger.info(f"Base Model Config: {base_model_config}")

            return base_model_config

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
    
    def get_model_trainer_config(self):
        try:
            model_trainer = self.config.model_trainer
            params = self.params
            base_model = self.config.base_model_preparation

            create_directories([model_trainer.root_dir])              ### Now always pass path to this function as list
            logger.info(f"Model Trainer directory created at {model_trainer.root_dir}")

            model_trainer_config = ModelTrainerConfig(
                root_dir = Path(model_trainer.root_dir),
                trained_model_path = Path(model_trainer.trained_model_path),
                updated_base_model_path = Path(base_model.updated_base_model_path),
                train_data_path= Path(model_trainer.train_data_path),
                test_data_path= Path(model_trainer.test_data_path),
                valid_data_path= Path(model_trainer.valid_data_path),
                augmentation = params.AUGMENTATION,
                image_size = params.IMAGE_SIZE,
                epochs = params.EPOCHS,
                batch_size = params.BATCH_SIZE,
                train_history_dir = Path(model_trainer.train_history_dir),
                loss_images_path = Path(model_trainer.loss_images_path),
                accuracy_images_path = Path(model_trainer.accuracy_images_path),
                history_json_path = Path(model_trainer.history_json_path)

            )
            logger.info(f"Model Trainer Config: {model_trainer_config}")
            
            return model_trainer_config
    
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)