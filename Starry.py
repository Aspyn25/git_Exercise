from turtledemo.sorting_animate import enable_keys

user = int(input("n : "))

# 1
for x in range(user):
    for y in range(user - x - 1):
        print(" ", end="") # blank / - 1 means print on first line
    for y in range(2*x+1): # * 1,3,5,7 pattern / odd number
        print("*", end="")
    print()

# 2
print("---------2----------")
for x in range(user, 0, -1):
    for y in range(x):
        print("*",end="")
    print()


########## I wanted to make symmetry shape from 3 to 5 (included even numbers)
# 3
print("---------3----------")
for x in range(1, user + 1): # start on first line
    if x > (user//2): # * decreasing from the maximum point
        # even number also can be made symmetry shape
        for j in range(user-x+1):
            print("*",end="")
    else: # * increasing
        for j in range(x):
            print("*",end="")
    print()


# 4
print("---------4----------")

for x in range(1, user + 1): # 1,8
    if x > (user//2): # * increasing
        for y in range(user - x + 1):
            print(" ", end="")
        for y in range(2 * x - user):
            print("*", end="")
    else: # * decreasing
        for y in range(x):
            print(" ", end="")
        for y in range(user - 2 * (x-1)):
            print("*", end="")
    print()

# 5
print("---------5----------")
# if user % 2 == 0:  # even numbers
mid = user // 2
for x in range(1, user + 1):
    if x <= mid:  # * increasing
        for y in range((user+1)//2 - x):
            print(" ", end="")
        for y in range(2 * x - 1):
            print("*", end="")
    else:  # * decreasing / 2 lines of middle can be made symmetry shape
        for y in range(x - mid - 1):
            print(" ", end="")
        for y in range(2 * (user - x) + 1):
            print("*", end="")
    print()
#
# else:  # odd numbers
#     mid = (user + 1) // 2
#     for x in range(1, user + 1):
#         if x < mid:  # * increasing
#             for y in range(mid - x):
#                 print(" ", end="")
#             for y in range(2 * x - 1):
#                 print("*", end="")
#         else:  # * decreasing
#             for y in range(x - mid ):
#                 print(" ", end="")
#             for y in range(2 * (user - x) + 1):
#                 print("*", end="")
#         print()
