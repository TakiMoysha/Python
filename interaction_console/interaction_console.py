from threading import Thread
import gevent
import time

from tick import Tick, TICKS
from commands_dict import commands_dict
import server

class IOThread(Thread):
    def __run__(self):
        scanner_command()


class ServerThread(Thread):
    def __run__(self):
        main()


def sixteen_ticks(*args):
    for i in range(60):
        activity()


def sixteen_ticks_per_second(*args):
    start_time = time.time()
    sixteen_ticks()
    wait_time = time.time() - start_time + 1
    if wait_time > 0:
        time.sleep(wait_time)


def activity():
    TICKS.increment()


def main():
    start_time = time.time()
    try:
        sixteen_ticks_per_second()
    except Exception as e:
        print(e)
    finally:
        print(f'{time.time() - start_time}:', str(TICKS))


def scanner_command():
    command = input("Command: ")
    commands_dict[command]("command")


def create_threads():
    io_thread = IOThread(name="io_thread+")
    server = ServerThread(name="server")
    threads = [io_thread, server]
    threads.start()


def run_server():
    server.run_server(port=int(54321))

if __name__ == "__main__":
    main()