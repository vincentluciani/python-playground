from abc import ABC, abstractmethod

from design_patterns.observer_pattern.observer import AbstractObserver


class AbstractSubject(ABC):
    _observers = set()

    #  add an observer to the list of observers
    def attach(self,observer):
        if not isinstance(observer,AbstractObserver):
            raise TypeError('Observer not derived from AbstractObserver')
        self._observers |= {observer}

    # take off an observer from the list of observers
    def detach(self,observer):
        self._observers -= {observer}

    # notify the subscribers that a new information was added
    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._observers.clear()
