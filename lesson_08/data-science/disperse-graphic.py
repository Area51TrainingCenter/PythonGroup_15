import matplotlib.pyplot as plt
import random

x = [i for i in range(50)]
random_list = []
for i in range(50):
    r = random.randint(0, 100)
    random_list.append(r)

fig, ax = plt.subplots()
ax.scatter(x, random_list)
ax.plot(x, x, color='red')

plt.show()
