from array import *

int_array = array("i", [1, 2, 3, 4, 5])
for i in int_array:
    print(i)
int_array.append(6)
for i in int_array:
    print(i)
int_extended_array = array("i", [7, 8, 9, 0])
int_array.extend(int_extended_array)
for i in int_array:
    print(i)
