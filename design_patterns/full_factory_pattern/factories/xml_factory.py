from design_patterns.full_factory_pattern.factories.abstract_factory import FullAbstractFactory
from design_patterns.full_factory_pattern.source_readers import  XMLParser


class JSONFactory(FullAbstractFactory):

    def create_parser(self):
        self.xml_parser = xml_parser = XMLParser()
        xml_parser.name = "XML"
        return xml_parser

