from design_patterns.full_factory_pattern.factories.abstract_factory import FullAbstractFactory
from design_patterns.full_factory_pattern.source_readers import JSONParser


class JSONFactoryFull(FullAbstractFactory):

    def create_parser(self):
        self.json_parser = json_parser = JSONParser()
        json_parser.name = "JSON"
        return json_parser
