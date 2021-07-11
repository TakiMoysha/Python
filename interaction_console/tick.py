class Tick():
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def __str__(self):
        return f'{self.value}'


TICKS = Tick()