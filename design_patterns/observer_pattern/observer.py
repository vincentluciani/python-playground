from abc import ABC, abstractmethod

class AbstractObserver(ABC):

    # react to a notification from the source of information
    @abstractmethod
    def update(self,value):
        pass

    def __enter__(self):
        return self

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass