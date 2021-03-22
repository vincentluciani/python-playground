from factories import loader

def test(factory_name):
    factory = loader.load_factory(factory_name)
    parser = factory.create_parser()
    parser.read("test")
    parser.display()

test("json_factory")
print("===")
test("xml_factory")
print("===")
test("lala")



