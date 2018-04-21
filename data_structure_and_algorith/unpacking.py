import math

help(math)

names = ["ajay", "ravi", "anita", "sagar"]

ajay, ravi, anita, sagar = names

print(ajay)
print(ravi)
print(anita)
print(sagar)

data = ["ajay", 50, 91.1, (7, 3, 1989)]

name, share, price, date = data
print(name)

p = (4, 5, 6)
x, y, z = p
_, m, _ = p
print(m)

grades = (1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7)


def drop_first_last(grades):
    first, *middle, last = grades
    return middle


print(drop_first_last(grades))
