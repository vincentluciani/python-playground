from unittest.mock import Mock

from injectable import (
    Injectable,
    load_injection_container, inject,
)
from injectable.testing import clear_injectables, register_injectables

from injectables.factory.vehicle_interface import Vehicle
from injectables.full_example.car import Car
from injectables.full_example.configuration import Configurator


def mock_configurator():
    clear_injectables(Configurator)
    mocked_configuration = Mock(wraps=Configurator)
    configuration = {
        'bicycle': {
            'speed_limit': '1000',
        },
        'car': {
            'speed_limit': '900'
        }
    }

    mocked_configuration.get_speed_limit = Mock(side_effect=lambda type: configuration.get(type, {}).get('speed_limit',''))
    mocked_configuration_injectable = Injectable(lambda: mocked_configuration)
    register_injectables({mocked_configuration_injectable}, Configurator)


def mock_car():
    clear_injectables("car")
    mocked_car = Mock(wraps=Car)
    mocked_car.forward = Mock(side_effect=lambda: print("driving but not for real"))
    mocked_car_injectable = Injectable(lambda: mocked_car)
    register_injectables({mocked_car_injectable}, qualifier="car")




def test_move_forward():
    test_vehicle: Vehicle = inject("car")
    test_vehicle.forward()

load_injection_container()

print(" === move with the real car")
test_move_forward()

print("=== move with the real car but fake configuration")
mock_configurator()
test_move_forward()

print("=== move with a fake car")
mock_car()
test_move_forward()
