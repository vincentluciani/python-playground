import unittest
from unittest.mock import Mock

from injectable import load_injection_container, Injectable, inject, autowired, Autowired
from injectable.testing import clear_injectables, register_injectables

from injectables.car import Car
from injectables.mocktest import RealCar
from injectables.vehicle_interface import Vehicle



# class TestWithMock(unittest.TestCase):
#
#     def test_with_mock_car(self):
#         load_injection_container("../")
#         clear_injectables("car")
#         mocked_car = Mock(wraps="car")
#         mocked_car.forward = Mock(side_effect=lambda: print("driving but not for real"))
#         mocked_injectable = Injectable(lambda: mocked_car)
#         register_injectables({mocked_injectable}, "car")
#
#         run_test()


class InjectableMocking():

    def __init__(self):
        pass
        clear_injectables(Car)
        mocked_car = Mock(wraps=Car)
        mocked_car.forward = Mock(side_effect=lambda: print("driving but not for real"))
        mocked_injectable = Injectable(lambda: mocked_car)
        register_injectables({mocked_injectable}, Car)

    @autowired
    def run(self, dep: Autowired(Car)):
            dep.forward()


def run_example():
    load_injection_container("../")
    example = InjectableMocking()
    example.run()


if __name__ == "__main__":
    run_example()

