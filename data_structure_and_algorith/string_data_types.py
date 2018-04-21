first_name = "ajay"
last_name = "kumar"

print(first_name + " " + last_name)

full_name = "Ajay Kumar"

print(full_name)
print(full_name[0])
print(full_name[0:5])
print(full_name[5:])

# sets in python
# mutable sets
basket = {"apple", "orange", "banana", "peer", "orange", "banana"}  # duplicate elements will be removed
print(basket)
basket.add("guava")
print(basket)

# frozen sets or immutable sets
cities = frozenset("patna")
print(cities)
# cities.add("california")  # adding new element causing error , new element cannot be added as sets are frozen one
# print(cities)


#  dictionary
user_dict = {"name": "ajay", "roll": "21", "dob": "7th march"}
print(user_dict)
print(user_dict["name"])
print(user_dict.values())
print(user_dict.keys())

#  tuple
user_tuple = ("ajay kumar", 21)
print(user_tuple)


# user_tuple[2] = "dav" # tuple object does not support item assignment so error
# print(user_tuple)


def func():
    """this function does nothing at all"""
    return


print(func.__doc__)  # accessing doc associated with function

help(func)  # accessing doc associated with this function


def greet(name, greeting="Hello"):
    # printing the greeting of user
    # name of the user
    print("{} {}".format(greeting, name))


print(greet.__doc__)  # comment won't provide any information about doc associated with function

help(greet)


def hello(name, language="en"):
    """
    
    generating documents for the function
    :param name: name of the person to be greeted 
    :param language: language in which person should be greeted
    :return: 
    """""
    print(name)


print(hello.__doc__)

# date time in python
import datetime

today = datetime.date.today()
now = datetime.datetime.now()
print(today ,now)
