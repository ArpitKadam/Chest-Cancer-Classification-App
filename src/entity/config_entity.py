from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    data_dir: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    augmentation: bool
    image_size: list
    learning_rate: float
    epochs: int
    batch_size: int
    num_classes: int
    include_top: bool
    weights: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    train_data_path: Path
    test_data_path: Path
    valid_data_path: Path
    augmentation: bool
    image_size: list
    epochs: int
    batch_size: int
    train_history_dir: Path
    loss_images_path: Path
    accuracy_images_path: Path
    history_json_path: Path