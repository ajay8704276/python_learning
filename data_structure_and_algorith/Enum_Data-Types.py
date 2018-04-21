from enum import Enum


class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


# different ways to access
print(Color.RED)
print(Color(1))
print(Color["RED"])

# iteration of enum
for c in Color:
    print(c)
