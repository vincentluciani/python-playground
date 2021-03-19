from injectable import injectable, Autowired, autowired
from  injectables.configuration import Configurator

from injectables.vehicle_interface import Vehicle


@injectable(qualifier="bicycle")
class Bicycle(Vehicle):
    @autowired
    def __init__(self, configuration: Autowired(Configurator)):
        # thanks to autowired it is not necessary to add the configuration argument
        # when calling _configure Bicycle()
        self.configuration = configuration

    def forward(self):
        print("going forward with a bicycle")
        print("speed limit:"+self.configuration.get_speed_limit('bicycle'))

