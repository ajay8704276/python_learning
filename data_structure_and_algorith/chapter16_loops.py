# i = 0
# while i < 7:
#     print(i)
#     if i == 4:
#         print("breaking from loop!")
#         break
#     i = i + 1
#     print(i)
#
# for i in (0, 1, 2, 3, 4):
#     print(i)
#     if i == 2:
#         break
#
# for i in (0, 1, 2, 3, 4, 5):
#     if i == 2 or i == 4:
#         continue
#     print(i)
#
# while True:
#     for i in range(1, 5):
#         if i == 2:
#             break
#
#
#
#

# def break_all_loops():
#     for j in range(1, 5):
#         for i in range(1, 4):
#             if i * j == 6:
#                 print(i * j)
#                 return i
#
#
# break_all_loops()
#
# for i in range(3):
#     print(i)
# else:
#     print("done")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")

# a = [1, 2, 3, 4, 5, "6"]
# for i in a:
#     if type(i) is not int:
#         print(i)
#         break
# else:
#     print("No Exception")


# d = {"a": 1, "b": 2, "c": 3}
#
# for key in d:
#     print(key)
#
# for key in d.keys():
#     print(key)
#
# for value in d.values():
#     print(value)
#

lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
for s in lst:
    print(s[:1])