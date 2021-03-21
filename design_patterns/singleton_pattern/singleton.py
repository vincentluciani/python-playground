class Singleton(object):
    _instances={}

    # cls represents the class that is needed to be instantiated,
    # and the compiler automatically provides this parameter at the time of instantiation
    # __new__ is called when creating the object, __init__ when initializing it
    # https://www.geeksforgeeks.org/__new__-in-python/
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]



