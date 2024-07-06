# Taking multiple argument using (*args)

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
#
# print(add(1, 2, 9, 10))


#simple exercise of (*args) taking multiple arguments at a same time
def concatenate_strings(*args):
    return " ".join(args)
print(concatenate_strings("Hello", "world"))         # Output should be "Hello world"
print(concatenate_strings("Python", "is", "fun"))    # Output should be "Python is fun"
print(concatenate_strings("OpenAI", "GPT-4"))        # Output should be "OpenAI GPT-4"

# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
