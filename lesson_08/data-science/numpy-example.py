import numpy as np

# creando un array a partir de un iterable
array = np.array([1, 2, 3, 4, 5])
print(array)

# usando método arange
array = np.arange(10.)
print(array)

# usando zeros y unos
zeros = np.zeros(10)
ones = np.ones(10)

print(zeros)
print(ones)

# usando linspace
array1 = np.linspace(0, 40, 5)
array2 = np.linspace(0, 40, 7)
print(array1)
print(array2)

# Aritmética

# producto con escalar

l1 = [1, 2, 3, 4, 5]
array1 = np.array(l1)
print(l1 * 5)
print(array1 * 5)

# suma

l2 = [5, 4, 3, 2, 1]
array2 = np.array(l2)
print(l1 + l2)
print(array1 + array2)

# producto
# print(l1 + l2) #  no trabaja
print(array1 * array2)

# concatenando

# print(np.concatenate(np.array([[1, 2, 3]]), np.array([[1, 2, 3]])))

# funciones utiles

print(np.max(array1))
print(np.min(array2))
print(np.mean(array1))
print(np.median(array2))

# types

print(type(array1))
print(type(array1[0]))
print(np.shape(array1))

# más de una dimension

bdarray = np.array([[1, 2, 3], [4, 5, 6]])
print(bdarray)
print(np.shape(bdarray))

# slicing

print(array1)
print(array1[1:])
print()
print(bdarray)
print(bdarray[1:, 1:])
