import os
import shutil
import datetime

def create_backup(folder_path):
    output_archive_name = f'backup-{os.path.basename(folder_path)}-{datetime.datetime.now().date()}'
    shutil.make_archive(output_archive_name, 'zip', folder_path)