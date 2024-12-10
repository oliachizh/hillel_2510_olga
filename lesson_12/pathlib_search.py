from pathlib import Path
import os
base_path = Path(__file__).parent.parent.parent

all_ = [k for k in base_path.iterdir()]

# print(*all_, sep='\n')
all_folders = [k for k in base_path.iterdir() if k.is_dir()]
# print(*all_folders, sep='\n')
all_files = [k for k in base_path.iterdir() if k.is_file()]
# print(*all_files, sep='\n')
find_logs_file = [k for k in base_path.iterdir() if k.is_file() and k.name.endswith('.log')]
print(*find_logs_file, sep='\n')
# print(Path.home())#Base user's directory
# print(find_logs_file[0].exists())#check if the path exists


all_logs = []

#alll files with .log
for dir_path, folders, files in os.walk(str(base_path)):
    for file_name in files:
        if file_name.endswith('.log'):
            all_logs.append(str(Path(dir_path, file_name)))

print(*all_logs, sep='\n')

