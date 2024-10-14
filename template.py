import os
from pathlib import Path
import logging
  
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s]')
project_name='textsummarzer'
list_of_files=[
    ".github/workflows/gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipline/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    'config/config.yaml',
    'params.yaml',
    'main.py',
    'app.py',
    'setup.py',
    'Dokerfile',
    'requrements.txt',
    'test.py'
    
]
for filepath in list_of_files:
    filepath = Path(filepath)#to handle both relative and absolute paths
    file_dir,filename=os.path.split(filepath)
#to check if the directory is not empty and make a new directory if it doesn't exist
    if file_dir !="":
         os.makedirs(file_dir, exist_ok=True)
         logging.info(f"creating directory: {file_dir}for the file {filename}")
#to create the file 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"created file: {filepath}")
    else:
        logging.info(f"file {filepath} already exists")
    