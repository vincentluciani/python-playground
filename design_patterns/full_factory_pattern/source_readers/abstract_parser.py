from abc import ABC, abstractmethod

class AbstractParser(ABC):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def read(self, input_string):
        pass

    @abstractmethod
    def display(self):
        pass