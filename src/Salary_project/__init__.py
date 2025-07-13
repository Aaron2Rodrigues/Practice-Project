import os
import logging
import sys

get_logger = '%(asctime)s: %(levelname)s: %(filename)s: %(message)s'

log_dir = 'logs'
log_filepath = os.path.join(log_dir,'logging.log')
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format=get_logger,
                    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
        ]
)

logger = logging.getLogger('projectlogger')
