class Director(object):
    def __init__(self, builder):
        self._builder = builder

    def build_thing(self):
        self._builder.build_thing()
        self._builder.step_1()
        self._builder.step_2()

    def get_thing(self):
        return self._builder.get_thing()
