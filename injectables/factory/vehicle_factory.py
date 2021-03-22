from injectable import injectable_factory

from injectables.full_example.car import Car
from injectables.factory.vehicle_interface import Vehicle


@injectable_factory(dependency=Vehicle,qualifier='vehicle_factory')
class VehicleFactory():
    def create_vehicle(self,type):
        if type == "car":
            return Car()


