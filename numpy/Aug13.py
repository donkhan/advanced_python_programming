import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

#print(a)
#print(np.flip(a, axis=0))

# Exchange First and Last Row
t = np.array(a[0:1, :])
a[0:1, :] = a[2:3, :]
a[2:3, :] = t
#print(a)

# Exchange First and Last Row


a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

#print(a)
# Col Swap
t = np.array(a[:, 0:1])
a[:, 0:1] = a[:, 2:3]
a[:, 2:3] = t
#print(a)


# Diagonals being 0
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

a = np.arange(1, 17).reshape(4, 4)
#print(a)

# Print 4 corners
#print(np.array(a[0:4:3, 0:4:3]).reshape(4))

# Extract Diagonals
a = np.arange(1,26).reshape(5,5)
#print(a)
#print(a[range(0, 5, 1), range(0, 5, 1)])

#print(a[range(0, 5, 1), range(4, -1, -1)])

# Replace Diagonal
#a[range(0, 5, 1), range(0, 5, 1)] = 0
#print(a)


# a = np.array([4,7,2,4,9,7,3,2,8,7]), find the unique elements that occur more than once.
a = np.array([4, 7, 2, 4, 9, 7, 3, 2, 8, 7])
values, counts = np.unique(a, return_counts=True)
#print(values[counts > 1])

# Given a = np.array([15,8,22,3,17,30,11,6,25]), extract elements that are even and greater
# than 10.
a = np.array([15, 8, 22, 3, 17, 30, 11, 6, 25])

#  Given a = np.array([[10,20,30],[40,50,60]]), append the row [70,80,90] using NumPy.
a = np.array([[10, 20, 30], [40, 50, 60]])
b = np.array([70,80,90]).reshape(1,3)
a = np.append(a,b, axis=0)

#print(a)

a = np.array([[10, 20, 30], [40, 50, 60]])
b = np.array([70,80]).reshape(2,1)
a = np.append(a,b, axis=1)
#print(a)

# a = np.arange(1,13), reshape it into 3 × 4 and then into 2 × 6
a = np.arange(1,13)
#print(a.reshape(3,4))
#print(a.reshape(2,6))

# a = np.arange(1,17).reshape(4,4), create a new array containing only elements greater than the mean of a.
a = np.arange(1,17).reshape(4,4)
#print(a[a > np.mean(a)])

#Given a = np.array([[4,8,12],[16,20,24],[28,32,36]]), find the row having the largest sum.
a = np.array([[4,8,12],[16,20,24],[28,32,36]])
#print(np.argmax(np.sum(a,axis=1)))

# Smallest sum
#print(np.argmin(np.sum(a,axis=1)))

#a = np.array([[2,5,8],[1,4,7],[3,6,9]]), find the elements that are greater than their row mean.
a = np.array([[2,5,8],[1,4,7],[3,6,9]])
rm = np.mean(a,axis=1).reshape(3,1)
#print(a[ a > rm])

#Given a = np.array([[10,15,20],[25,30,35],[40,45,50]]), replace every element divisible by 5 with 0.
a = np.array([[10,15,20],[25,30,35],[40,45,50]])
a [ a % 5 == 0] = 0
#print(a)

# Given a = np.array([[10,20,30],[40,50,60],[70,80,90]]), create [10 50 90] using NumPy
#indexing. Then create [30 50 70] without manually writing the values.

a = np.array([[10,20,30],[40,50,60],[70,80,90]])
#print(a[np.arange(3), np.arange(3)])


#print(np.arange(1,26))
a = np.arange(1,26).reshape(5,5)
a[2,2] = -1
#print(a)

a = np.arange(1,37).reshape(6,6)
#print(a[0:6:2,0:6:2])


a = np.array([[12,45,23,17],[56,21,34,10],[18,39,27,44]])
#print(np.argmax(a,axis=1))


a = 5
b = 10
#print(a,b)
(a,b) = (b,a)
#print(a,b)


a = np.array([[10,20,30],[40,50,60],[70,80,90]])
#print(a)
#a[[0,-1]] = a[[-1,0]]
#print(a)

t = np.array(a[:,0])
a[:,0] = a[:,-1]
a[:, -1] = t
#print(a)
#a = np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]]), without a
#loop produce [10 40 70 100 130 160] using NumPy indexing/slicing. Then produce [40 70 100 130].


a = np.array([[10, 20, 30, 40], [50, 60, 70, 80],[90, 100, 110, 120], [130, 140, 150, 160]])
#print(np.concat((np.array([a[0,0]]), a[range(0, 4, 1), range(3, -1, -1)], np.array([a[3,3]])), axis=0))
