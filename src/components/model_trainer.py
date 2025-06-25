from src.logger import logger
from src.exception import CustomException
import os, sys
import tensorflow as tf
from keras.callbacks import EarlyStopping, ModelCheckpoint
from src.entity.config_entity import ModelTrainerConfig
from pathlib import Path
from src.utils import create_directories, save_json
import matplotlib.pyplot as plt

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def get_model(self):
        try:
            self.model = tf.keras.models.load_model(
                self.config.updated_base_model_path
            )
            logger.info(f"Model loaded successfully from {self.config.updated_base_model_path}")
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

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
    def save_model(path: Path, model: tf.keras.Model):
        try:
            model.save(path)
            logger.info(f"Model saved at {path}")
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)

    def get_data_for_training(self):
        try:
            self.train_data = tf.keras.preprocessing.image_dataset_from_directory(
                directory=self.config.train_data_path,
                batch_size=self.config.batch_size,
                interpolation = "bilinear",
                image_size = self.config.image_size[:-1],
                label_mode="categorical",
                shuffle=True
            )
            logger.info(f"Data loaded successfully from {self.config.train_data_path}")

            self.valid_data = tf.keras.preprocessing.image_dataset_from_directory(
                directory=self.config.valid_data_path,
                batch_size=self.config.batch_size,
                interpolation = "bilinear",
                image_size = self.config.image_size[:-1],
                label_mode="categorical",
                shuffle=False
            )
            logger.info(f"Data loaded successfully from {self.config.valid_data_path}")

            self.test_data = tf.keras.preprocessing.image_dataset_from_directory(
                directory=self.config.test_data_path,
                image_size=self.config.image_size[:-1],
                interpolation="bilinear",
                batch_size=self.config.batch_size,
                label_mode="categorical",
                shuffle=False
            )
            logger.info(f"Data loaded successfully from {self.config.test_data_path}")
        
        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
    
    def train(self):
        try:
            early_stopping = EarlyStopping(
            monitor='val_loss',
            patience=8,
            restore_best_weights=True
            )
            logger.info(f"Early stopping initialized")

            checkpoint = ModelCheckpoint(
                filepath=str(self.config.trained_model_path),
                monitor='val_loss',
                save_best_only=True
            )
            logger.info(f"Model checkpoint initialized")

            logger.info(f"Training started")
            self.history = self.model.fit(
                self.train_data.map(ModelTrainer.normalize_img),
                validation_data=self.valid_data.map(ModelTrainer.normalize_img),
                epochs=self.config.epochs,
                callbacks=[early_stopping, checkpoint],
                )
            logger.info(f"Training completed")
            
            self.save_model(path=self.config.trained_model_path, model=self.model)
            logger.info(f"Model saved at {self.config.trained_model_path}")

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
    
    def save_training_metrics(self):
        try:
            history_dir = Path(self.config.train_history_dir)
            metrics_path = self.config.history_json_path
            loss_image = self.config.loss_images_path
            acc_image = self.config.accuracy_images_path

            create_directories([history_dir])
            logger.info(f"History directory created at {history_dir}")

            history_dict = self.history.history
            logger.info(f"History dictionary created")
            logger.info(f"History dictionary: {history_dict}")

            save_json(path=metrics_path, data=history_dict)
            logger.info(f"Metrics saved at {metrics_path}")

            plt.figure(figsize=(10, 8))
            plt.plot(history_dict['loss'], label='Train Loss')
            plt.plot(history_dict['val_loss'], label='Val Loss')
            plt.title('Loss Over Epochs')
            plt.xlabel('Epochs')
            plt.ylabel('Loss')
            plt.legend() 
            plt.savefig(loss_image)
            plt.close()
            logger.info(f"Loss plot saved to {loss_image}")

            plt.figure(figsize=(10, 8))
            plt.plot(history_dict['accuracy'], label='Train Accuracy')
            plt.plot(history_dict['val_accuracy'], label='Val Accuracy')
            plt.title('Accuracy Over Epochs')
            plt.xlabel('Epochs')
            plt.ylabel('Accuracy')
            plt.legend()
            plt.savefig(acc_image)
            plt.close()
            logger.info(f"Accuracy plot saved to {acc_image}")

        except Exception as e:
            logger.error(e)
            raise CustomException(e, sys)
    