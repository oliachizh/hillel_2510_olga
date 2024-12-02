# import logging
#
# # Налаштування конфігурації логування
# # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#
# # Додавання обробника для виводу в консоль
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.CRITICAL)
# formater = logging.Formatter('!!!!!!!%(asctime)s - %(levelname)s - %(message)s')
# console_handler.setFormatter(formater)
#
# logging.getLogger('').addHandler(console_handler)
#
# # Логування подій різного рівня
# logging.debug('Це повідомлення рівня DEBUG')
# logging.info('Це повідомлення рівня INFO')
# logging.warning('Це повідомлення рівня WARNING')
# logging.error('Це повідомлення рівня ERROR')
# logging.critical('Це повідомлення рівня CRITICAL')

import logging
import logging.config
import os
from utils import BASE_DIR

logging.config.fileConfig(os.path.join(BASE_DIR, 'logging_config.ini'))

# Використання логера
sample_logger = logging.getLogger('sampleLogger')
#
# logger.debug('Це повідомлення рівня DEBUG')
# logger.info('Це повідомлення рівня INFO')