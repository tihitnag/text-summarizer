#entity return type it will retrun this variable 
#custome retun type
from dataclasses import dataclass
from pathlib import Path 

@dataclass(frozen=True)
class DataIngestionconfig:
    root_dir: Path 
    source_urls: str
    local_data_files:Path
    unzip_dir:Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path 
    status_file: str
    required_file:list 
    