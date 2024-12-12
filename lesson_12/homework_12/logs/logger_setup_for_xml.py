import logging

# Створення конфігурації
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),  # Виведення в консоль
                    ])

# Використання логера
logger = logging.getLogger(__name__)