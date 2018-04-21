restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
print(restaurants)

# converts list to sets of unique value
unique_restaurants = set(restaurants)
print(unique_restaurants)

# converts set to list
unique_list = list(unique_restaurants)
print(unique_list)

a = {1, 2, 2, 3, 4}
b = {3, 3, 4, 4, 5}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

c = {1, 2}
print(c.issubset(a))
print(a.issuperset(c))

# Counter from collection module
from collections import Counter

counterList = Counter(['a', 'b', 'b', 'c'])
print(counterList)
