from injectable import load_injection_container, inject

from injectables.factory.vehicle_interface import Vehicle
from injectables.full_example.car import Car

load_injection_container()

test_vehicle: Vehicle = inject("bicycle")
test_vehicle.forward()

test_vehicle: Vehicle = inject("car")
test_vehicle.forward()







