from design_patterns.builder_pattern.my_abstract_builder import AbstractBuilder
from design_patterns.builder_pattern.my_thing import MyThing


class MyBuilder2(AbstractBuilder):

    def step_1(self):
        print("step 1")
        self._thing.my_property_1="1b"
    def step_2(self):
        print("step 2")
        self._thing.my_property_2="2b"


