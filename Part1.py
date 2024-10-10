num = int(input("put the number : "))
n = int(input("put the n : "))

# print("The n-th digit is", num%(10**n)//(10**(n-1)))

# using for loop
for i in range(n):
    if i == n-1:
        num = num % 10
        break
    num = num // 10
    #print(num)

print("The n-th digit is",num)


# find the pattern
# num = 123456
# find_num = 0
# # // : quotient, % : remainder
# # 1 : 6
# print(num%10//1)
#
# # 2 : 5
# print(num%100//10)
#
# # 3 : 4
# print(num%1000//100)
#
# # 4 : 3
# print((num%10000)//1000)

