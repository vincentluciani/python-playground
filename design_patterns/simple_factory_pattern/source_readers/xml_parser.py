from design_patterns.simple_factory_pattern.source_readers.abstract_parser import AbstractParser


class XMLParser(AbstractParser):
    def read(self, input_string):
        self.input_string = input_string

    def display(self):
        print("xml parser result:"+self.input_string)