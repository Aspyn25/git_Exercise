height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# weight / height ** 2
bmi = [] 

for num in range(0,len(height)):
    bmi.append(round(weight[num] / height[num] ** 2),2)

print(bmi)

users = [[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, 68.7]]

bmi_2 = []
for i in range(len(users[0])):
    bmi_2.append(round(users[1][i] / users[0][i] ** 2, 2))

print(bmi_2)