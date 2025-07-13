import os
import logging
from pathlib import Path

name = 'Salary_project'

logging.basicConfig(level=logging.INFO , format= '%(asctime)s %(message)s]')

list_of_folders = [
    '.github/workflows/.gitkeep',
    f'src/{name}/__init__.py',
    f'src/{name}/config/__init__.py',
    f'src/{name}/config/configuration.py',
    f'src/{name}/components/__init__.py',
    f'src/{name}/components/components.py',
    f'src/{name}/entity/__init__.py',
    f'src/{name}/entity/config_entity.py',
    f'src/{name}/utils/__init__.py',
    f'src/{name}/utils/common.py',
    f'src/{name}/pipeline/__init__.py',
    f'src/{name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'template/index.html',
]

for fol in list_of_folders:
    filepath = Path(fol)
    filedir,filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filepath,exist_ok=True)
        logging.info(f'Creating directory {filedir} for file {filename} ')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f'Creating empty file {filename}')

    else:
        logging.info(f'Already exists')


