import time
# асинхронные вызовы в сеть (gevent, asyncio, aiohttp)
import aiohttp
import asyncio
import gevent

def print_lead_time(function):
    def run_lead_time(*args):
        start_time = time.time()
        function()
        print(f'{function.__name__}: {time.time() - start_time}')
    return run_lead_time


@print_lead_time
async def create_session():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_session())
