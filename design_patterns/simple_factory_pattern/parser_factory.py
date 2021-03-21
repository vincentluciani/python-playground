from inspect import getmembers, isclass, isabstract

from design_patterns.simple_factory_pattern.source_readers.abstract_parser import AbstractParser

# source_readers is a folder in the same directory as this file
# it has an init file containing imports to concrete parsers
import source_readers

class ParserFactory(object):
    # the key is the parser name and the value is the specific parser's class
    list_of_parsers = {}
    def __init__(self):
        self.load_parsers()

    def load_parsers(self):
        # The getmembers() function retrieves the members of an object such as a class or module
        # the object, source_readers, is the import of the folder containing all the parsers
        # we want to list only the classes, not the interfaces
        classes =  getmembers(source_readers, lambda m:isclass(m) and not isabstract(m))

        # getmembers gives a list of class names + class type
        # we add them to the list of parsers only if it is a class
        # and if it is a child of the abstract parser class
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, AbstractParser):
                self.list_of_parsers.update([[name, _type]])

    # self.list_of_parsers[parser_name] gives the real class which name is parser_name
    # self.list_of_parsers[parser_name]() is an instance of this class self.list_of_parsers[parser_name]
    def create_instance(self, parser_name):
        if parser_name in self.list_of_parsers:
            return self.list_of_parsers[parser_name]()
        else:
            return source_readers.NullParser(parser_name)
