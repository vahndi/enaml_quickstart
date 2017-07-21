from atom.atom import Atom
from atom.scalars import Bool, Callable, Float, FloatRange, Int, Long, Range, Str, Unicode, Value
from atom.containerlist import ContainerList
from atom.dict import Dict
from atom.enum import Enum


class MainModel(Atom):

    message = Str()

    def __init__(self):

        self.message = 'Hello World!'


