# 🫁 Chest Cancer Classification App

A full-stack deep learning project that classifies chest X-ray images into various cancer categories using TensorFlow/Keras. It integrates **data versioning (DVC)**, **model tracking**, **Docker**, and a **Flask-based web interface**, with CI/CD workflows through **GitHub Actions** and remote storage on **DAGsHub**.

---

## 📌 Features

- 🧠 Deep Learning CNN model using transfer learning (EfficientNet)
- 📦 Modular codebase with pipeline stages (`data_ingestion`, `base_model`, `training`, `evaluation`)
- 🚀 Real-time prediction web app using **Flask**
- 📈 Model evaluation and confidence scores
- 🔁 Reproducible experiments with **DVC**
- 🐳 Dockerized for seamless deployment
- ☁️ Remote artifact storage using **DAGsHub**
- ⚙️ GitHub Actions for CI/CD automation

---

## 📁 Project Structure

<details>
<summary>Click to expand/collapse</summary>
  
```
└── arpitkadam-chest-cancer-classification-app/
    ├── README.md
    ├── __init__.py
    ├── app.py
    ├── demo.py
    ├── Dockerfile
    ├── dvc.lock
    ├── dvc.yaml
    ├── LICENSE
    ├── main.py
    ├── params.yaml
    ├── requirements.txt
    ├── setup.py
    ├── template.py
    ├── .dockerignore
    ├── .dvcignore
    ├── artifacts/
    │   ├── base_model/
    │   │   ├── base_model.h5
    │   │   └── updated_base_model.h5
    │   ├── data_ingestion/
    │   │   └── data.zip
    │   ├── model_evaluation/
    │   │   └── evaluation_scores.json
    │   └── model_trainer/
    │       ├── trained_model.h5
    │       └── model_history/
    │           └── model_history.json
    ├── config/
    │   ├── config.yaml
    │   ├── model.yaml
    │   └── schema.yaml
    ├── Research/
    │   └── research.ipynb
    ├── src/
    │   ├── __init__.py
    │   ├── components/
    │   │   ├── __init__.py
    │   │   ├── base_model.py
    │   │   ├── data_ingestion.py
    │   │   ├── model_evaluation.py
    │   │   └── model_trainer.py
    │   ├── configuration/
    │   │   ├── __init__.py
    │   │   └── configuration.py
    │   ├── constants/
    │   │   └── __init__.py
    │   ├── entity/
    │   │   ├── __init__.py
    │   │   ├── artifact_entity.py
    │   │   └── config_entity.py
    │   ├── exception/
    │   │   └── __init__.py
    │   ├── logger/
    │   │   └── __init__.py
    │   ├── pipeline/
    │   │   ├── __init__.py
    │   │   ├── prediction_pipeline.py
    │   │   └── training_pipeline.py
    │   └── utils/
    │       └── __init__.py
    ├── templates/
    │   ├── home.html
    │   ├── importance.html
    │   └── prediction.html
    ├── .dvc/
    │   └── config
    └── .github/
        └── workflows/
            └── main.yaml
```
</details>

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/ArpitKadam/Chest-Cancer-Classification-App.git
cd Chest-Cancer-Classification-App
```

### 2. Create and Activate Virtual Environment
```bash
conda create -n tensor python=3.10 -y
conda activate tensor
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Training Pipeline
```bash
python main.py
```

### 5. Launch Web Application
```bash
python app.py
```
Navigate to: http://127.0.0.1:8080

---

## 📦 Docker Usage

### Build Docker Image
```bash
docker build -t arpitkadam/chest-cancer-app:latest .
```

### Run Container
```bash
docker run -p 8080:8080 arpitkadam/chest-cancer-app:latest
```

---

## 💾 DVC Workflow

### Setup Remote (only once)
```bash
dvc remote add -d storage https://dagshub.com/ArpitKadam/Chest-Cancer-Classification-App.dvc
```

### Reproduce pipeline and push data
```bash
dvc repro
dvc push
```

---

## ⚙️ CI/CD

GitHub Actions configured in `.github/workflows/main.yaml` for:

- Linting and testing
- Pushing data to DAGsHub
- Auto-retraining (optional)

---

## 🧪 Model Metrics

Evaluation scores are saved in: `artifacts/model_evaluation/evaluation_scores.json`

<details>
<summary>Click to expand/collapse</summary>

```
{
    "loss": 0.5021160244941711,
    "accuracy": 0.7684127163887024
}
```

</details>

---

## 📂 DVC Tracked Artifacts

- `data_ingestion/data.zip`
- `base_model/base_model.h5`
- `model_trainer/trained_model.h5`
- `model_history/model_history.json`
- `model_evaluation/evaluation_scores.json`

---

## 📄 License

This project is licensed under the [Apache-2.0 license](https://github.com/ArpitKadam/Chest-Cancer-Classification-App/blob/main/LICENSE).

---

## ✨ Author

**Arpit Sachin Kadam**

- 💼 [LinkedIn](https://linkedin.com/in/arpitkadam)
- 🌐 [Portfolio](https://arpit-kadam.netlify.app/)
- 📦 [GitHub](https://github.com/ArpitKadam)
- 🧪 [DAGsHub](https://dagshub.com/ArpitKadam)

---

## 🙌 Contributions

Contributions are welcome! Please open issues or submit a PR.

---

## 🔧 Tech Stack

- **Deep Learning**: TensorFlow/Keras, VGG19
- **Web Framework**: Flask
- **Data Versioning**: DVC
- **MLOps**: DAGsHub
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Frontend**: HTML, CSS, JavaScript

---

## 📊 Usage Examples

### Command Line Prediction
```bash
python main.py
```

### Web Interface
1. Upload chest X-ray image
2. Get classification results with confidence scores
3. View model interpretation and importance maps

---

## 🚨 Important Notes

- Ensure you have sufficient GPU memory for training
- The model is trained on chest X-ray images - ensure input images are in the correct format
- For production deployment, consider implementing additional security measures
- Regular model retraining is recommended as new data becomes available

---

## 📈 Future Enhancements

- [ ] Add more cancer types for classification
- [ ] Implement model explainability features (LIME/SHAP)
- [ ] Add user authentication and session management
- [ ] Integrate with medical imaging standards (DICOM)
- [ ] Add batch processing capabilities

