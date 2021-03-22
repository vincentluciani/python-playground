import abc
import inspect
from abc import ABC, abstractmethod



import abc
from abc import ABC, abstractmethod

class FullAbstractFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_processor(self):
        pass


class ClassExample(FullAbstractFactory):
    def create_processor(self):
        pass

# Test general behaviour.
print( inspect.isabstract(FullAbstractFactory))
print(inspect.isabstract(ClassExample))
