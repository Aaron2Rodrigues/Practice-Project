from pathlib import Path
import os
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from src.Salary_project import logger
import yaml
from typing import Any
import json

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            context = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {yaml_file} loaded sucessfully')
            return ConfigBox(context)
    except BoxValueError as e:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_create: list , verbose = True):
    
    for path in path_to_create:
        os.makedirs(path , exist_ok=True)
        if verbose:
            logger.info(f'Directory : {path_to_create} created sucessfully')

@ensure_annotations
def save_json(path : Path , data : dict):
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
    logger.info(f'Created json file to : {path}')

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path) as f:
        context = json.load(f)
    logger.info(f'loaded json file sucessfully')
    return ConfigBox

@ensure_annotations
def save_joblib(path: Path, data: Any):
    joblib.dump(value=data , filename=path)
    logger.info(f'joblib file saved: {path}')

@ensure_annotations
def load_joblib(path:Path)-> Any:
    data = joblib.load(path)
    logger.info(f'file loaded from: {path}')
    return data