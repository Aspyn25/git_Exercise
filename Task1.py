import numpy as np
#1
# arr1 = np.array(range(1,31))
arr1 =[x for x in range(1,31)]
arr = np.array(arr1)
print(arr, arr.shape)
print(arr[10])

#2
print("---------2---------")
arr = arr.reshape(6,5)
print(arr)
print(arr[3,4])

#3
print("---------3---------")
print(arr[2])
print(arr[:2,-3:])

#4
print("---------4---------")
arr_4 = np.array(np.random.randint(10,100,15))
print(arr_4)
print(max(arr_4), min(arr_4))

#5
print("---------5---------")
arr_5 = np.array(np.random.randint(0,50,16)).reshape(4,4)
print(arr_5)
print(np.sum(arr_5))

#6
print("---------6---------")
arr_6 = np.random.randint(1,20,25).reshape(5,5)
print(arr_6)
arr_6[1,] = 0
print(arr_6)
arr_6[arr_6>10] = 99
print(arr_6)

#7
print("---------7---------")
arr_7 = np.array(np.random.randint(1,10,5))
arr_7_1 = np.array(np.random.randint(1,10,5))
print(arr_7)
print(arr_7_1)

print(np.add(arr_7,arr_7_1),np.subtract(arr_7,arr_7_1),np.multiply(arr_7,arr_7_1))

#8
print("---------8---------")
num = [2,4,6,8]
arr_8 = np.array(num)
arr_8_1 = np.array(np.random.randint(1,5,12).reshape(3,4))
print(arr_8)
print(arr_8_1)
print(arr_8+arr_8_1)

#9
print("---------9---------")
arr_9 = np.array(np.random.randint(1,100,20))
print(arr_9)
print(arr_9[arr_9>50])
arr_9[arr_9<30] = -1
print(arr_9)

#10
print("---------10---------")
arr_10 = np.array(np.random.randint(1,50,12))
print(arr_10.reshape(3,4))
print(arr_10.reshape(4,3))

# 10. Task 10 Reshaping Arrays
# Create a 1D array of 12 random integers between 1 and 50. Reshape the array into a 34 2D array.
# Transpose the array (swap rows and columns) and print the result.