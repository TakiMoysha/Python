import os
import json
import time

import logging

import asyncio
import aiofiles

import aiohttp

# format = "%(asctime)s - %(file_path) - %(message)s"
logging.basicConfig(format='%(asctime)s: %(message)s')

KEY = 'angle'
WRONG_KEY = 'an'


async def create_async_tasks(file_path):
    async with aiofiles.open(file_path) as file:
        content = await file.read()

    js_file = json.loads(content)
    try:
        js_file[KEY]
    except KeyError:
        message = f"File: {file_path} - wrong key"
        logging.warning(message)


def async_starter(paths):
    event_loop = asyncio.get_event_loop()
    tasks = [event_loop.create_task(create_async_tasks(path)) for path in paths]
    # event_loop.set_task_factory(tasks)
    event_loop.run_until_complete(asyncio.wait(tasks))


if __name__ == "__main__":
    data_dir_path = os.path.abspath('file_reading_async/data')
    files = os.listdir(data_dir_path)
    start_point = time.time()

    paths = tuple(map((lambda file: f'{data_dir_path}\\{file}'), files))[:6000]
    async_starter(paths)

    print(f"Work time: {time.time() - start_point}")
