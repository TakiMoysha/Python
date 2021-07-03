import time

# асинхронные вызовы в сеть (gevent, asyncio, aiohttp)
import aiohttp
import asyncio
import gevent

def print_lead_time(function):
    def lead_time(*args):
        start_time = time.time()
        function(*args)
        print(f'{function.__name__}: {timel.time() - start_time}')


@print_lead_time
async def create_session():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_session())
