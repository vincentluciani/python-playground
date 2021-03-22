from design_patterns.simple_factory_pattern.source_readers.abstract_parser import AbstractParser


class JSONParser(AbstractParser):
    def read(self, input_string):
        self.input_string = input_string

    def display(self):
        print(f"json parser result (parser name {self.name}):{self.input_string}")
