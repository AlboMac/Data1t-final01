import os
from datetime import datetime
import argparse

def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', default='User')
    parser.add_argument('-p', '--path', default='/')

    return parser
parser = createparser()
namespace = parser.parse_args()
path = namespace.path

name = namespace.name
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Hello, {name}!\nCurrent time: {current_datetime}")


file_count = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print(f"количество файлов по указанному пути: {file_count}")


list_of_files = sorted((os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))),
                   key=lambda f: os.path.getsize(f), reverse=True)[:10]
print("Top 10 largest files (in KB):")
for i, file in enumerate(list_of_files, start=1):
    size_kb = os.path.getsize(file) / 1024
    print(f"Топ-10 файлов по размеру в указанном пути:{i}. {file}: {size_kb:.2f} KB")
