from abc import ABC, abstractmethod

from design_patterns.builder_pattern.my_thing import MyThing


class AbstractBuilder(ABC):

    def get_thing(self):
        return self._thing

    def build_thing(self):
        self._thing = MyThing()

    @abstractmethod
    def step_1(self):
        pass

    @abstractmethod
    def step_2(self):
        pass