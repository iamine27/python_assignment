# With __slots__, the attribute names are stored in a tuple-like structure,
# allowing for more efficient memory usage, instead of dictionary
# the attributes allowed in an instance, the attribute lookup
# and assignment become faster
# Attribute Restriction


class Person:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Alex", 33)
print(person.name)
print(person.age)

person.address = "Paris, 75020"  # Error should be raised
