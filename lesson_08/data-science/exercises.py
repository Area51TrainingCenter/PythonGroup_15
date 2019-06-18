import numpy as np

array = np.array([[2, 4, 5, 6], [0, 3, 7, 4], [8, 8, 5, 2], [1, 5, 6, 1]])
print(array)
print(array[1])
subarray = array[:3, :3]
mask = [True, False, True]
print(subarray[mask])
