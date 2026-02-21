# from pathlib import Path 

# CONFIG_FILE_PATH =Path('config/config.yaml')
# PARAMS_FILE_PATH =Path('C:/End-To-End-MLOPS-Data-Science-Project-Implementation-With-Deployment/params.yaml')#Path('params.yaml')
# SCHEMA_FILE_PATH=Path('C:/End-To-End-MLOPS-Data-Science-Project-Implementation-With-Deployment/schema.yaml')#Path('schema.yaml')

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"
SCHEMA_FILE_PATH = PROJECT_ROOT / "schema.yaml"