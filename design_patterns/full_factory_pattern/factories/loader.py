from importlib import import_module
from inspect import getmembers, isclass, isabstract
import inspect

# must be the exact same import as in the files containing the factories
from design_patterns.full_factory_pattern.factories.abstract_factory import FullAbstractFactory


def load_factory(factory_name):
    try:
        # Import a module dynamically from the factories folder
        factory_module = import_module('.'+factory_name,'factories')
    except ImportError:
        factory_module = import_module('.null_factory','factories')

    # Get all classes ( no abstract classes ) from the imported module
    classes = getmembers(factory_module,
                         lambda m:isclass(m)  and not isabstract(m))


    # From these classes, get all classes that are child of AbstractFactory
    for name, _class in classes:
        if issubclass(_class, FullAbstractFactory):
            return _class()


