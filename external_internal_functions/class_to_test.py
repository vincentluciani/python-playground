import external_functions


class ClassToTest():

    def __init__(self):
        self.external_object = external_functions.ExternalObject()

    def give_result(self):


        return self.external_object.external_function()


