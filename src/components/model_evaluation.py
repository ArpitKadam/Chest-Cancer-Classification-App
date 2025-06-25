from src.entity.config_entity import EvaluationConfig
from src.logger import logger
from src.exception import CustomException
from src.configuration.configuration import AppConfig
import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from src.utils import save_json
import sys

class ModelEvaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
    
    @staticmethod
    def normalize_img(image, label):
        try:
            image = tf.cast(image, tf.float32) / 255.0
            logger.info(f"Image normalized successfully")
            return image, label
        
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        try:
            logger.info(f"Loading model from {path}")
            return tf.keras.models.load_model(path)
        
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
    
    def get_test_data(self):
        try:
            self.test_data = tf.keras.preprocessing.image_dataset_from_directory(
                directory=self.config.test_data_path,
                image_size=self.config.image_size[:-1],
                interpolation="bilinear",
                batch_size=self.config.batch_size,
                label_mode="categorical",
                shuffle=False
            )

            self.test_data = self.test_data.map(ModelEvaluation.normalize_img)
            logger.info(f"Test data loaded successfully from {self.config.test_data_path}")

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
    
    def evaluate(self):
        try:
            self.model = self.load_model(self.config.model_path)
            logger.info(f"Model loaded successfully from {self.config.model_path}")

            self.results = self.model.evaluate(self.test_data)
            logger.info(f"Model evaluated successfully")

            self.score = {'loss': self.results[0], 'accuracy': self.results[1]}
            logger.info(f"Model score: {self.score}")

            save_json(path=Path(self.config.score_file), data=self.score)
            logger.info(f"Score saved at {self.config.score_file}")

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
    
    def log_into_mlflow(self):
        logger.info(f"Logging into mlflow")
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        logger.info(f"Tracking url type store: {tracking_url_type_store}")

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(self.score)
            mlflow.log_artifact(local_path=self.config.score_file)
            mlflow.log_artifact(local_path=self.config.loss_images_path)
            mlflow.log_artifact(local_path=self.config.accuracy_images_path)
            mlflow.log_artifact(local_path=self.config.history_json_path)

            if tracking_url_type_store != "file":
                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
            else:
                mlflow.keras.log_model(self.model, "model")

            logger.info(f"Model logged into mlflow")
            mlflow.end_run()

if __name__ == "__main__":
    try:
        config = AppConfig()
        eval_config = config.get_evaluation_config()
        evaluation = ModelEvaluation(eval_config)
        evaluation.get_test_data()
        evaluation.evaluate()
        evaluation.log_into_mlflow()
    
    except Exception as e:
        raise CustomException(e, sys)