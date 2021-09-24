import tm_test_module
from time import time


def measured_time(func):
    def wrapper(arg1):
        start_time = time()
        func(arg1)
        end_time = time() - start_time
        print(func.__name__, end_time)

    return wrapper


@measured_time
def python_run(n):
    if (n <= 1):
        return n
    return python_run(n-1) + python_run(n-2)


@measured_time
def c_run(n):
    return tm_test_module.c_fib(n)


if __name__ == "__main__":
    tm_test_module.__verions__
    # python_res = python_run(1)
    # c_res = c_run(1)

    # print(f"python_res: {python_res}")
    # print(f"c_res: {python_res}")
