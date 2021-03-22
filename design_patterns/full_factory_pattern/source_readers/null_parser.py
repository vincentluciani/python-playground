from design_patterns.simple_factory_pattern.source_readers.abstract_parser import AbstractParser


class NullParser(AbstractParser):

    def __init__(self, parser_name):
        self.parser_name = parser_name

    def read(self, input_string):
        print("Unknown parser:"+ self.parser_name)

    def display(self):
        pass