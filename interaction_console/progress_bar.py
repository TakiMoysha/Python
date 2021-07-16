import time
import sys

from clint.textui import progress

def show_progress(value: int, symbol: str = '*'):
    sys.stderr.write(f'[{str(symbol*value)}]\r')

if __name__ == '__main__':
    # using library
    for i in progress.bar(range(30)):
        time.sleep(.5)
