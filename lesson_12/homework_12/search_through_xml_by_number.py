import xml.etree.ElementTree as ET
from logs.logger_setup_for_xml import logger
from pathlib import Path

files_path = Path(__file__).parent.parent
files_folder = ['files']
filepath = Path(str(files_path), *files_folder,'groups.xml')

"""
Для файла ideas_for_test/work_with_xml/groups.xml 
створіть функцію пошуку по group/number 
і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""

def load_xml_file(filepath):
    # Завантаження XML-файлу
    try:
        tree = ET.parse(filepath)
        return tree.getroot()
    except ET.ParseError as e:
        logger.error(f"Failed to parse XML file: {e}")
        return None
    except FileNotFoundError:
        logger.info(f"File {filepath} is not found")
        return None



def find_incoming_value_by_group_num(number, filepath):
# Читання та виведення даних з елементів XML-документу
    root = load_xml_file(filepath)
    if root is not None:
        for group in root:
            num = group.find('number').text
            if num == str(number):
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find(('incoming'))
                    logger.info(f"incoming value is {incoming.text}")
                    return incoming.text
                else:
                    logger.info(f"timingExbytes value for group with number {number} is: {timing_exbytes}")
    else:
        logger.info("Can't load XML file")



