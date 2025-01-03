import logging
import os
from pathlib import Path

current_file_path_folder = Path(__file__).parent
new_folder = Path(current_file_path_folder, "log_files")
new_folder.mkdir(exist_ok=True)

# Створення конфігурації
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(new_folder, 'logs.log'))  # Запис у файл
                    ])

# Використання логера
logger = logging.getLogger(__name__)
