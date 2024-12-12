from pathlib import Path
import json
from logs.logger_setup import logger

files_path = Path(__file__).parent.parent
files_folder = ['files']
filepath = Path(str(files_path), *files_folder,'localization_en.json')

def check_json_is_valid(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            valid_json = json.dumps(data)
        if valid_json != data:
            logger.error(f"Checking if json is valid in file: {filepath}")
            logger.error(data)
            return False
        else:
            return True
    except FileNotFoundError:
        logger.error(f"File: {filepath} is not found")
    except json.JSONDecodeError as exc:
        logger.error(f"Decode error: {exc}")



