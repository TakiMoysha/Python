import os

def get_output_path(filename: str):
    OUTPUT_PATH = os.path.abspath(f'./pdf/{filename}')
    return OUTPUT_PATH