import numpy as np

a = np.array([
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
])

ab = np.array([
    [8, 11, 6],
    [3, 5, 7],
    [17, 19, 25]
])

n = 3
rs = np.array([])
cs = np.array([])
dia_1 = 0
dia_2 = 0

for i in range(n):
    c = 0
    for j in range(n):
        c = c + a[i, j]
        r = c + a[j, i]
        if i == j:
            dia_1 = dia_1 + a[i, j]
        if i + j == n-1:
            dia_2 = dia_2 + a[i, j]
    cs = np.append(cs, np.array([c]))
    cs = np.append(rs, np.array([r]))

X = np.append(np.append(np.append(rs, cs), np.array([dia_1])),np.array([dia_2]))
#print(np.all(X == np.sum(a) // n)
d1 = np.trace(a)
X = np.append(
    np.append(
        np.append(np.sum(a, axis=1), np.sum(a, axis=0)),
        np.array([dia_2])),
    np.array([dia_1]))
print(X)
print(np.all(X == np.sum(a) // n))

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Swapping
print(a)
t = np.array(a[0:1, :])
a[0:1, :] = a[2, :]
a[2, :] = t
#print(a)

a = 12
b = 23
(a,b) = (b,a)
#print(a, b)


a = np.array([[4, 8, 12], [16, 20, 24], [28, 32, 36]])
print(np.argmax(np.sum(a, axis=0), axis=0))

a = np.array([[102,15,20],[25,30,35],[40,45,50]])
print(a)
a = np.where(a % 5 == 0, 1, a)
print(a)


