print("I like coffee")

import matplotlib.pyplot as plt

list01 = [1, 2 , 3, 4]
list02 = [ 50, 108, 162, 250]

plt.scatter(x = list01, y = list02)
plt.xlabel("semester")
plt.ylabel("credits")
plt.title('Title')
plt.savefig('./my_plot.png') # save a copy of the figure to the PyCharm project directory (./ is a relative directory).
plt.show()

