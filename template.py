import os
from pathlib import Path

project_name = 'src'

files = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "main.py",
    "app.py",
    "__init__.py",
    "Research/research.ipynb",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/configuration.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "params.yaml"
    "config/model.yaml",
    "config/schema.yaml",
    "config/config.yaml",
    ".env",
    "dvc.yaml"
]

for file_path in files:
    file = Path(file_path)
    
    # Create parent directories if they don't exist
    if not file.parent.exists():
        os.makedirs(file.parent, exist_ok=True)
        print(f"Creating directory: {file.parent}")

    # Create the file if it does not exist or is empty
    if not file.exists() or file.stat().st_size == 0:
        file.touch()
        print(f"Creating empty file: {file}")
    else:
        print(f"File {file} already exists and is not empty, skipping creation.")