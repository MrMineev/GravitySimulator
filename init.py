import numpy as np

with open('AI/good_launch/actions.txt', 'r') as file:
    datay = file.readlines()

    mas = []

    for i in range(len(datay)):
        mas.append(int(datay[i]))
    
    datay = np.array(mas)

    file.close()

on = False
for index in range(0, len(datay)):
    if datay[index] == 1:
        on = True
    elif datay[index] == 2:
        on = False

    if datay[index] == -1 and on == True:
        datay[index] = 1

with open('AI/good_launch/actions.txt', 'w') as file:
    for index in range(0, len(datay)):
        file.write(f"{datay[index]}\n")

