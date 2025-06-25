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