


def convert(type):
    def convertor(f):
        def wrapper_function(*args,**kwargs):
            result_before_modification=f(*args,**kwargs)
            if type == "string":
                return str(result_before_modification)
            elif type == "integer":
                return int(result_before_modification)
        return wrapper_function
    return convertor

@convert("integer")
def multiply_by_two(*args,**kwargs):
    return 2*kwargs.get("input")


print(multiply_by_two(input=2))


