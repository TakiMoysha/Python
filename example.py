import time
from functools import lru_cache

class Cahir():
    pass


def lead_time(fun):
    def lead_time_run(number: int):
        start_time = time.time()
        returned = fun(number)
        print(f'{fun.__name__} - {time.time() - start_time}')
        return returned
    return lead_time_run

def msh_cache(fun):
    def msh_cache_run():
        pass
    return msh_cache_run


# @lru_cache
# @lead_time
def rucursive_factorial(number: int) -> int:
    if (number <= 1):
        return 1
    return number*rucursive_factorial(number-1)


@lead_time
def factorial(number: int) -> int:
    if (number <= 1):
        return 1
    result = 1
    for i in range(1, number+1):
        result *= i
    return result

if __name__ == "__main__":
    print(type("asd"))
    print(type(Cahir))
    print(type(factorial))