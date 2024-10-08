def add(*args):
    print(args[0])

    sum = 0
    for n in args:
       sum += n
    return sum

print(add(3, 5,6))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items()
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n*= kwargs["mulipy"]


calculate(add=3, mulitpy=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)