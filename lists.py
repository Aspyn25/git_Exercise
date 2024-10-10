# 1
list1 = [10, 20, 30, 40, 50]
for x in list1:
    print(x)


# 2
list2 = [1, 2, 3, 4, 5]
sum = 0
for x in list2:
    sum += x
print(sum)

# 3
list3 =  [3, 7, 2, 9, 4]
large_num = 0
for x in list3:
    if large_num < x:
        large_num = x
print(large_num)

# 4
list4 = [1, 4, 4, 2, 4, 3]
cnt = 0
for i in list4:
    if i == 4:
        cnt += 1
print("4:",cnt)

# 5
list5 = [1, 2, 3, 4, 5]
new = []
for x in list5:
    new.append(x**2)
print(new)

# 6
list6 = ["Python", "is", "awesome"]
str = ""
for x in list6:
    str = str + x + " "
print(str)

# 7
list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = []
for x in list7:
    if x % 2 == 0:
        n.append(x)
print(n)

# 8
list8 = [2, 4, 6, 8]
ne = []
for x in list8:
    ne.append(x*2)
print(ne)

# 9
list9 =[1, 3, 3, 4, 3, 5, 3]
while 3 in list9:
    list9.remove(3)
print(list9)

# 10
list10 = [5, 7, 8, 7, 10]
cnt = 0
for i, v in enumerate(list10):
    if v == 7:
        print(i)
        break
