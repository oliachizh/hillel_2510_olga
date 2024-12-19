from pathlib import Path
import json
from logs.logger_setup import logger

files_path = Path(__file__).parent.parent
files_folder = ['files']
filepath = Path(str(files_path), *files_folder,'localization_en.json')

def check_json_is_valid(filepath):
    try:
        with open(filepath, 'r') as file:
            try:
               data = json.load(file)
               return True
            except json.JSONDecodeError:
                logger.error(data)
                return False
    except FileNotFoundError:
        logger.error(f"File: {filepath} is not found")
        print(f"Error: File '{filepath}' not found.")
    except Exception as exc:
        logger.error(f"error: {exc}")



