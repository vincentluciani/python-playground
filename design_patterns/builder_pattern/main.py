from design_patterns.builder_pattern.director import Director
from design_patterns.builder_pattern.my_builder import MyBuilder
from design_patterns.builder_pattern.my_builder_2 import MyBuilder2

my_thing_builder = Director(MyBuilder())

my_thing_builder.build_thing()
my_thing = my_thing_builder.get_thing()
my_thing.display()


my_thing_builder = Director(MyBuilder2())

my_thing_builder.build_thing()
my_thing = my_thing_builder.get_thing()
my_thing.display()

