def worker(file_path):
    f = json.load(open(file_path))
    try:
        f[KEY]
    except KeyError:
        message = f"File: {file_path} - wrong key"
        logging.warning(message)
