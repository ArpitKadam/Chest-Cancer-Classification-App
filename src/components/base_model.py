from src.logger import logger
from src.exception import CustomException
import sys
import tensorflow as tf
from src.entity.config_entity import PrepareBaseModelConfig
from pathlib import Path

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        try:
            model.save(path)
            logger.info(f"Model saved at {path}")

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def download_base_mode(self):
        try:
            self.model = tf.keras.applications.VGG19(
                input_shape=self.config.image_size,
                include_top=self.config.include_top,
                weights=self.config.weights,
            )
            logger.info(f"Model downloaded successfully")

            self.save_model(path=self.config.base_model_path, model=self.model)
            logger.info(f"Model saved at {self.config.base_model_path}")

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
    
    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        try:
            logger.info(f"Freeze all set to: {freeze_all} and Freeze till set to: {freeze_till}")
            if freeze_all:
                for layer in model.layers:
                    model.trainable = False
            elif (freeze_till is not None) and (freeze_till > 0):
                for layer in model.layers[:-freeze_till]:
                    model.trainable = False
                
            flatten_in = tf.keras.layers.Flatten()(model.output)
            prediction = tf.keras.layers.Dense(
                units=classes,
                activation="softmax"
            )(flatten_in)

            full_model = tf.keras.models.Model(
                inputs = model.input,
                outputs = prediction
            )

            full_model.compile(
                optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=['accuracy']
            )

            full_model.summary()
            logger.info(f"Model summary: {full_model.summary()}")
            logger.info(f"Model compiled successfully")
            
            return full_model

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def update_base_model(self):
        try:
            self.full_model = self._prepare_full_model(
                model = self.model,
                classes = self.config.num_classes,
                freeze_all=True,
                freeze_till=None,
                learning_rate=self.config.learning_rate
            )
            logger.info(f"Model updated successfully")

            self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
            logger.info(f"Updated Model saved at {self.config.updated_base_model_path}")
        
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)