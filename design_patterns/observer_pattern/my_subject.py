from design_patterns.observer_pattern.subject import AbstractSubject

# specific subject (inherits from abstract subject)
# contains information to be forecasted
class MySubject(AbstractSubject):
    _info_1 = -1
    _info_2 = -1

    @property
    def info_1(self):
        return self._info_1

    @property
    def info_2(self):
        return self._info_2

    # set the information to be forecasted
    def set_attributes(self, info_1, info_2):
        self._info_1 = info_1
        self._info_2 = info_2
        self.notify()  # calls the notify function ( this class is inheriting from Abstract subject)
