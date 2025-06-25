import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import os, sys
from src.exception import CustomException
from src.logger import logger
from keras.utils import load_img, img_to_array


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        try:
            model = load_model(os.path.join("artifacts", "model_trainer", "trained_model.h5"))

            imagename = self.filename
            test_image = load_img(imagename, target_size=(224, 224))
            test_image = img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis=0)
            
            result = model.predict(test_image)
            predicted_class = np.argmax(result, axis=1)[0]
            confidence_scores = result[0].tolist()

            class_names = ["adenocarcinoma", "large cell carcinoma", "normal", "squamous cell carcinoma"]

            return {
                "predicted_class": class_names[predicted_class].upper(),
                "confidence_scores": {
                    class_names[i]: round(float(conf), 4)
                    for i, conf in enumerate(confidence_scores)
                }
            }
                

        except Exception as e:
            raise CustomException(e, sys)