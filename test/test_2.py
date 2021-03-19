import unittest

from injectable import load_injection_container, inject

from injectables.vehicle_interface import Vehicle


class ThisIsMyTest(unittest.TestCase):
    def test_this_second_thing(self):

        load_injection_container("../")
        test_vehicle: Vehicle = inject("bicycle")
        test_vehicle.forward()

        test_vehicle: Vehicle = inject("car")
        test_vehicle.forward()
