import csv
from pathlib import Path
import os

files_folder = ['files']
files_path = Path(__file__).parent.parent

# Відкриття CSV-файлу для читання
filepath_1 = os.path.join(files_path, *files_folder,'random.csv')
filepath_2 = os.path.join(files_path, *files_folder,'random_michels.csv')

def read_files(file):
    with open(file, newline='') as csvfile:
        return list(csv.reader(csvfile))


def find_not_dublicated_elements_from_file(filepath_1, filepath_2):
        reader_1 = read_files(filepath_1)
        reader_2 = read_files(filepath_2)
        unic_rows = set()

        with open('output.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for row in reader_1:
                print(row)
                row_str = ','.join(row)
                if row_str not in unic_rows:
                    writer.writerow(row)
                    unic_rows.add(row_str)
            for row in reader_2:
                row_str = ','.join(row)
                if row_str not in unic_rows:
                    writer.writerow(row)
                    unic_rows.add(row_str)


find_not_dublicated_elements_from_file(filepath_1, filepath_2)
