from src.logger import logger
from src.exception import CustomException
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import yaml
import joblib
import base64
import os, sys
import json

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)

@ensure_annotations
def create_directories(path_to_directories: list, verbose=False):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at: {path}")
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)

@ensure_annotations
def save_json(path: Path, data: dict):
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"json file saved at: {path}")
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try:
        with open(path) as json_file:
            content = json.load(json_file)
        logger.info(f"json file loaded successfully from: {path}")
        return ConfigBox(content)
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)

@ensure_annotations
def save_bin(data: Any, path: Path):
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"binary file saved at: {path}")
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)

@ensure_annotations
def load_bin(path: Path) -> Any:
    try:
        data = joblib.load(path)
        logger.info(f"binary file loaded from: {path}")
        return data
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)

@ensure_annotations
def get_size(path: Path) -> str:
    try:
        size_in_kb = round(os.path.getsize(path)/1024)
        return f"~ {size_in_kb} KB"
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)

@ensure_annotations
def decode_image(imgstring, file_path):
    try:
        imgdata = base64.b64decode(imgstring)
        with open(file_path, 'wb') as f:
            f.write(imgdata)
        return file_path
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)

@ensure_annotations
def encode_image_into_base64(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            base64_data = base64.b64encode(file_data).decode('utf-8')
            return base64_data
    except Exception as e:
        logger.error(e)
        raise CustomException(e, sys)