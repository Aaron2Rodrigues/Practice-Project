import os
import logging
from pathlib import Path

name = 'Salary_project'

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s]')

list_of_files = [
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

<<<<<<< HEAD
for file_path in list_of_files:
    filepath = Path(file_path)
    filedir = filepath.parent

    #  Create parent directories
    os.makedirs(filedir, exist_ok=True)
    logging.info(f'Ensured directory {filedir} exists for file {filepath.name}')

    # Create the file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Created empty file {filepath.name}')
    else:
        logging.info(f'{filepath.name} already exists')
=======
for fol in list_of_folders:
    filepath = Path(fol)
    filedir, filename = os.path.split(filepath)

    # 🛠 Fix: Create the directory (not the file path)
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory {filedir} for file {filename}')

    # ✅ Create empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating empty file {filename}')
    else:
        logging.info(f'File {filename} already exists')
>>>>>>> 3c70f7d9fcb4cba3898af30c76499da5e1b20f56
