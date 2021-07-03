import inspect
import sys

from .msh_data import Model

class L(Model):
    def __init__(self, name):
        self.name = name

s = L("asdf")
print(inspect.isclass(L))