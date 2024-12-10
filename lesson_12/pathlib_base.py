from pathlib import Path
current_path_incorrect = Path('/lessons/lesson_12/pathlib_base.py')
# print(current_path.name)
# print(current_path.parts)
current_path_correct = Path(__file__)
print(current_path_correct)
BASE_DIR = Path(__file__).parent.parent.parent
print(BASE_DIR)
folder_to_log = ['logs', 'december']
file_name = 'file.log'
# path_to_log = Path(str(BASE_DIR), 'log', file_name)
path_to_log = Path(str(BASE_DIR), *folder_to_log, file_name)
print(path_to_log)
# print(path_to_log.exists()) # check whether file exists