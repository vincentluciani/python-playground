from abc import ABC, abstractmethod

class AbstractParser(ABC):

    @abstractmethod
    def read(self, input_string):
        pass

    @abstractmethod
    def display(self):
        pass