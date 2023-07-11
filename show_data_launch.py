import matplotlib.pyplot as plt
import numpy as np
from operations import operations
import math

with open('AI/good_launch/observations.txt', 'r') as file:
    datax = file.readlines()

    mas = []

    for i in range(len(datax)):
        qwe = datax[i].split()
        for g in range(len(qwe)):
            qwe[g] = float(qwe[g])
        
        mas.append(qwe)
    
    datax = np.array(mas)

    file.close()

with open('AI/good_launch/actions.txt', 'r') as file:
    datay = file.readlines()

    mas = []

    for i in range(len(datay)):
        mas.append(int(datay[i]))
    
    datay = np.array(mas)

    file.close()

print(f"datax => {datax}")
print(f"datay => {datay}")

on = False

N = 3000

index = 0
for data_point in datax:
    if index > N:
        break
    x = data_point[0]
    y = data_point[1]

    if datay[index] == 1:
        plt.plot(x, y, marker='o', color='red')
    else:
        plt.plot(x, y, marker='o', color='blue')

    index += 1

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plotting a Point')
plt.grid(True)

plt.show()

