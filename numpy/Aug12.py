import numpy as np

a = np.array([12, 5, 18, 7, 25, 3, 14, 9, 30])
a = np.where(a < 10, -1, np.where(a > 20, 1, a))


a = np.arange(1, 26).reshape(5, 5)
a[1:4, 1:4] = 0

a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

a = np.array([
    [12, 45, 23, 17],
    [56, 21, 34, 10],
    [18, 39, 27, 44]
])

# Q4
#print(np.max(a, axis=1))
#print(np.argmax(a, axis=1))





