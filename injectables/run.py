from injectable import load_injection_container, Autowired, inject

from injectables.vehicle_interface import Vehicle


load_injection_container()

test_vehicle: Vehicle = inject("bicycle")
test_vehicle.forward()

test_vehicle: Vehicle = inject("car")
test_vehicle.forward()







