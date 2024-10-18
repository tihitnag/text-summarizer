import os
from ensure import ensure_annotations
# to make sure we see the error in terms of data type
from box.exceptions import BoxKeyError
from textsummarzer.logging import logger
import yaml
from box import ConfigBox  # 'ConfigBox' for accessing config files with dot notation
from pathlib import Path  # Corrected 'Path' with capital 'P'
from typing import Any 

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(content)  # Correct 'ConfigBox'
    except BoxKeyError as e:
        raise ValueError('Error accessing keys in the YAML file')  # Handle 'BoxKeyError' more meaningfully
    except Exception as e:
        raise e

@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
    try:
        for path in path_to_directory:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f'directory: {path} created')
    except Exception as e:
        raise e

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f'{size_in_kb} KB'
