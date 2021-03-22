from abc import ABC, abstractmethod

from design_patterns.full_factory_pattern.factories.abstract_factory import FullAbstractFactory
from design_patterns.full_factory_pattern.source_readers import NullParser


class NullFactory(FullAbstractFactory):

    def create_parser(self):
        self.null_parser = null_parser = NullParser("NULL")
        return null_parser

