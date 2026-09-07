import numpy as np
# 1 Divide every element by the sum of its own row.
a = np.array([
    [2, 4, 6],
    [3, 6, 9],
    [5, 10, 15]
])
#print(a / np.sum(a, axis=1).reshape(3, 1))


a = np.array([
    [12, 45, 23],
    [56, 21, 34],
    [18, 39, 27]
])
a[range(0, 3, 1), np.argmax(a, axis=0)] = 0
#print(a)


# For each row, replace elements greater than that row's mean with -1
a = np.array([
    [10, 20, 30],
    [5, 15, 25],
    [40, 50, 60]
])
rm = np.mean(a, axis=1).reshape(3,1)
a[ a > rm] = -1
#print(a)


# Print boundary elements in clock wise direction
ar = np.arange(1, 26).reshape(5, 5)
#print(ar)

a = ar[0, 0]
b = ar[0, 1:4]
c = ar[0, 4]
d = ar[1:4, 4]
e = ar[4,4]
f = ar[4,3:0:-1]
g = ar[4,0]
h = ar[3:0:-1,0]
#print(a,b,c,d,e,f,g,h)

# Second Largest Element
a = np.array([
    [12, 45, 23],
    [56, 21, 34],
    [18, 39, 27]
])
a = np.unique(a)[-2]
#print(a)

a = np.array([
    [10, 20, 30],
    [5, 15, 25],
    [40, 50, 60],
    [7, 8, 9]
])

# symmetry check
a = np.array([
    [1, 2, 33],
    [2, 5, 6],
    [32, 6, 12]
])
#print(np.all(a == a.T))

print(np.count_nonzero(a % 2 == 0, axis=1).argmax())

a = np.array([
    [0,1,2], [3,4,5]
])

print(np.sum(a,axis=1))