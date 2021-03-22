from injectable import injectable, Autowired, autowired
from injectables.full_example.configuration import Configurator

from injectables.factory.vehicle_interface import Vehicle


@injectable(qualifier="car")
class Car(Vehicle):
    @autowired
    def __init__(self, configuration: Autowired(Configurator)):
        # thanks to autowired it is not necessary to add the configuration argument
        # when calling _configure Bicycle()
        self.configuration = configuration

    def forward(self):
        print("going forward with a car")
        print("speed limit:"+self.configuration.get_speed_limit('car'))


