import csv
from pathlib import Path

files_folder = ['files']
files_path = Path(__file__).parent.parent

filepath_1 = Path(str(files_path), *files_folder,'random.csv')
filepath_2 = Path(str(files_path), *files_folder,'random_michels.csv')


def read_files(file):
    with open(file, newline='') as csvfile:
        return list(csv.reader(csvfile))

def write_files(rows):
    with open('output.csv', 'w') as csvfile:
        writer =  csv.writer(csvfile)
        for row in rows:
            writer.writerow(list(row))


def find_not_dublicated_elements_from_file(*files):
        try:
            unic_rows = set()
            list_to_write = []
            for file in files:
                reader = read_files(file)
                for row in reader:
                    row_str = ','.join(row)
                    if row_str not in unic_rows:
                        unic_rows.add(row_str)
                        list_to_write.append(row)
                write_files(list_to_write)

        except FileNotFoundError:
            print('File is not found')
        except Exception as exc:
            print(f'Error {exc}')


find_not_dublicated_elements_from_file(filepath_1, filepath_2)
