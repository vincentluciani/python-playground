def outer():
    x = 3

    def inner(y):
        return x + y
    return inner(2)

def augment(multiplier):
    def multiply(x):
        return x*multiplier
    return multiply

mynewfunction = augment(3)

test = mynewfunction(2)
teststr = str(test)

print(teststr)
print("hello")
