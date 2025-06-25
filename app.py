from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from src.pipeline.training_pipeline import Train
from src.utils import decode_image
from src.pipeline.prediction_pipeline import PredictionPipeline

# Environment settings
os.environ['LANG'] = 'en_US.UTF-8'
os.environ['LC_ALL'] = 'en_US.UTF-8'

# Flask app initialization
app = Flask(__name__)
CORS(app)

# Global config
INPUT_IMAGE_NAME = "inputImage.jpg"


class ClientApp:
    def __init__(self, filename):
        self.filename = filename
        self.classifier = PredictionPipeline(self.filename)


# Initialize ClientApp instance
clApp = ClientApp(INPUT_IMAGE_NAME)


# Pages
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/predict-page", methods=["GET"])
def predict_page():
    return render_template("prediction.html")

@app.route("/importance", methods=["GET"])
def importance_page():
    return render_template("importance.html")


# Functional routes
@app.route("/train", methods=["GET", "POST"])
def train_route():
    train = Train()
    train.train()
    return jsonify({"message": "Training completed successfully!"})

@app.route("/predict", methods=["POST"])
def predict_route():
    try:
        data = request.get_json(force=True)
        image_data = data.get("image")

        if not image_data:
            return jsonify({"error": "No image data provided"}), 400

        decode_image(image_data, clApp.filename)
        prediction = clApp.classifier.predict()

        return jsonify(prediction)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
