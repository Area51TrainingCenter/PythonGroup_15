import matplotlib.pyplot as plt

x = [i for i in range(10)]
y = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]
n = len(x)

px = sum(x) / n
py = sum(y) / n
ssxy = 0
for i in range(n):
    ssxy += (x[i] - px) * (y[i] - py)
ssxx = 0
for i in range(n):
    ssxx += (x[i] - px) ** 2

b1 = ssxy / ssxx
b0 = py - b1 * px
print(b0)
print(b1)
hx = [b0 + i * b1 for i in range(n)]

fig, ax = plt.subplots()
ax.scatter(x, y, color='m')
ax.plot(x, hx, color='green')

plt.show()
