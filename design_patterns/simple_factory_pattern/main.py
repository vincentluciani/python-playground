from design_patterns.simple_factory_pattern.parser_factory import ParserFactory

factory = ParserFactory()


parser = factory.create_instance("JSONParser")
parser.read("test")
parser.display()

parser = factory.create_instance("XMLParser")
parser.read("test")
parser.display()



