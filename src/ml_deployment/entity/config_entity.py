from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:  #return type of entity
    root_dir:Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path