from injectable import injectable, autowired


@injectable(singleton=True)
class Configurator():
    def __init__(self):
        self.configuration = {'bicycle':{
            'speed_limit':'10',
        },
            'car':{
                'speed_limit':'90'
            }
        }
    def get_speed_limit(self,vehicle_type):

        return self.configuration.get(vehicle_type).get('speed_limit')



