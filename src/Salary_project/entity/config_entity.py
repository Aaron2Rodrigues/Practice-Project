from dataclasses import dataclass
from pathlib import Path 

@dataclass
class DataIngestionConfig:
    """ Path to access the raw data """
    root_dir:Path    
    """ Path to store the raw data """   
    input_path:Path
    """ Path to store the processed data """
    output_path:Path