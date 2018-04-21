a = "Hello Ajay!"
b = "Hello Ajay!"

if a == b:
    print("both a and b are equal by value")

if a is b:
    print("both a and b are not equal by reference!")

a = b

if a is b:
    print("both and b are equal by reference!")


# comparing objects

class Foo(object):
    def __init__(self, item):
        self.myitem = item

    def __eq__(self, other):
        return self.myitem == other.myitem


a = Foo(5)
b = Foo(5)
print(a == b)  # True
print(a != b)  # False
print(a is b)  # False
