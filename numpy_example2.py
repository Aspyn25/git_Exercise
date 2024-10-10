import numpy as np
from numpy.ma.core import around

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# print(type(height))

np_height = np.array(height)
np_weight =  np.array(weight)
print(type(np_height))

print(np_height > 1.75) # boolean
print(np_height[np_height > 1.75]) # element with condition

np_bmi = around(np_weight / np_height ** 2, 2)
print(np_bmi)

bb = np.array( [[1.73, 1.68, 1.71, 1.89, 1.791],[ 65.4, 59.2, 63.6, 88.4, 68.711]])
print(bb[1])