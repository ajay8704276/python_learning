def counter():
    num = 0

    def incrementer():
        nonlocal num
        num += 1
        return num

    return incrementer()


print(counter())

#  Global Variable Scope

x = "Hi"


def change_local_x():
    global x  # to make variable available globally use key word global
    x = "Bye"
    print(x)


change_local_x()
print(x)


# Local Variable

def foo():
    if True:
        a = 1
        print(a)


print(foo())

b = 2


def boo():
    if False:
        b = 3
        print(b)


print(boo())

local_var = 1


def local_variable():
    local_var = 2
    print(local_var)
    print(globals()['local_var'])
    local_var = 3
    print(local_var)
    global local_var

local_variable()
