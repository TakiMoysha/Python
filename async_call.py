from asyncio.events import get_event_loop
import time
# асинхронные вызовы в сеть (gevent, asyncio, aiohttp)
from aiohttp import web
import asyncio
from aiohttp.client import request
import gevent
import requests
import time


class Network:
    def __init__(self) -> None:
        self.session = requests.Session()

    async def get(self, url):
        return self.session.get(url)


async def question(net):
    math_sum = sum([1, 2, 3, 1, 2, 1, 3, 4, 5, 7, 2, 2])
    response = await net.get("https://question-it.com")


async def coderoad(net):
    response = await net.get("https://coderoad.ru/")


if __name__ == "__main__":
    start_time = time.time()
    loop = get_event_loop()
    net = Network()
    tasks = [coderoad(net), question(net)]
    loop.run_until_complete(asyncio.gather(*tasks))
    print(time.time() - start_time)