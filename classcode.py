print("I like coffee")

#import packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#variable and types######################################################################################

height = 6.0
weight = 170

bmi = weight / height**2
print(bmi)
type(bmi)

#int
x = 5
print(type(x))



#list example
list01 = [1, 2 , 3, 4]
list02 = [ 50, 108, 162, 250]

#example for list: list of height for a group
#list splicing, the 2 is excluded in the code: 0, 1 is spliced.
list03 = list01[0:2]
print(list03)

#list subset
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

print(house[4][1])

#copy list
#this will create same list and both will change with updates.
list04 = [1, 2 , 3, 4]
list05= list04

#this will make separate list
list06 = list(list04)

#FUNCTIONS#####################################################################################

help(max)
max(list05)

#rounds to one decimal place
round(1.67, 1)
#rounds to nearest integer if no ndigit is placed.
round(1.67)
#len() finds length
len(list05)
#sort() place in order
sorted(list05)
sorted(list05, reverse=True)

#scatter plot example
# plt.scatter(x = list01, y = list02)
# plt.xlabel("semester")
# plt.ylabel("credits")
# plt.title('Title')
# plt.savefig('./my_plot.png') # save a copy of the figure to the PyCharm project directory (./ is a relative directory).
# plt.show()

#https://github.com/ghwcore/BIOS-584/blob/main/Quiz_01.ipynb

list_enemies = ['water', 'purgatory', 'sun',  ]



