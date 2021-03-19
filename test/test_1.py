from unittest.mock import Mock
from external_internal_functions import external_functions
from external_internal_functions.class_to_test import ClassToTest

import unittest

class ThisIsMyTest(unittest.TestCase):
    def test_this_thing(self):

        mystub = Mock(external_functions.ExternalObject)
        mystub.external_function.return_value = 5
        mytest = ClassToTest()
        result = mytest.give_result()
        print("my result:"+str(result))
