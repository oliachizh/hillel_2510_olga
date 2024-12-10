from pathlib import Path

current_file_path_folder = Path(__file__).parent

#create new folder
new_folder = Path(current_file_path_folder, "new_folder")
new_folder_2 = Path(current_file_path_folder, "new_folder","new_folder_2", "new_folder_3")
new_folder.mkdir(exist_ok=True)
new_folder_2.mkdir(exist_ok=True, parents=True)