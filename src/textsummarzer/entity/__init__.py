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

@dataclass(frozen=True)
class DataTransforamtionConfig:
     root_dir:Path
     data_path: Path
     tokenizer_name: Path
@dataclass(frozen=True)
class ModelTrainConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs:int
    warmup_steps  :int
    per_device_train_batch_size  :int
    weight_decay:int
    logging_steps:int
    evaluation_strategy:int
    eval_steps:int
    save_steps:int
    gradient_accumulation_steps:int
    
class ModelEvaluationConfig:
    root_dir: Path
    data_path : Path
    model_path : Path
    tokenizer_path : Path
    metric_file_name : Path 