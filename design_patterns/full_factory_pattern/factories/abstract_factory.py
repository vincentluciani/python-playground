from abc import ABC, abstractmethod

class FullAbstractFactory(ABC):

    @abstractmethod
    def create_parser(self):
        pass

