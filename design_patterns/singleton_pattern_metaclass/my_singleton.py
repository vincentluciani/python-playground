from design_patterns.singleton_pattern_metaclass.singleton import Singleton


class MySingleton(metaclass=Singleton):
    my_param = None

    def __init__(self, external_param):
        if self.my_param is None:  # taken from the first created instance ( second and next are not instanciated )
            self.my_param = "test with param:"+str(external_param)

    def display_text(self, a_param):
        print(self.my_param + "-" + a_param)

