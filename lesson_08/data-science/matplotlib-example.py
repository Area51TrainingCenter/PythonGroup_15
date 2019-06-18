import matplotlib.pyplot as plt

x = [i for i in range(20)]
y = [i * i for i in range(20)]
fig, ax = plt.subplots()
ax.plot(x, y, label='cuadratic', marker='.')
y.reverse()
ax.plot(x, y, label='cuadratic inverse', color='green')
ax.legend()

plt.show()
