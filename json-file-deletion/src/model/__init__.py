import re
import os

from .backup import create_backup

def select_path():
    # path = os.path.abspath(input("Folder name: "))
    path = os.path.abspath('dataset')
    if not os.path.exists(path): return
    return path


path = select_path()
regex_pattern = '[0-9a-fA-F]+.json'
json_files = filter(lambda x: not re.match(regex_pattern, x), os.listdir(path))
for i in json_files: os.remove(os.path.join(path, i))