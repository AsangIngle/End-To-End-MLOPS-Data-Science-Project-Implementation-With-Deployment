from src.ml_deployment.components import *
from src.ml_deployment.utils.common import read_yaml,create_directories
from src.ml_deployment.entity.config_entity import DataIngestionConfig
from src.ml_deployment.constants import *


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH
    ):
        self.config_filepath = config_filepath
        self.params_filepath = params_filepath
        self.schema_filepath = schema_filepath
        
        self.config=read_yaml(self.config_filepath)
        self.params=read_yaml(self.params_filepath)
        self.schema=read_yaml(self.schema_filepath)
        
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )
        
        return data_ingestion_config