from examples.factory.external_client import ExternalClient as ExternalClient
from injectable import load_injection_container, inject, autowired, Autowired
from car import Car
from injectables.vehicle_factory import VehicleFactory


class Factory():
    @autowired
    def __init__(
            self,
            vehicle_factory: Autowired('vehicle_factory'),
    ):
        self.vehicle_factory = vehicle_factory

    def run(self):
        print("hello world")
        my_vehicle = self.vehicle_factory.create_vehicle("car")
        my_vehicle.forward()

def run_example():
    load_injection_container()

    example = Factory()
    example.run()


if __name__ == "__main__":
    run_example()


