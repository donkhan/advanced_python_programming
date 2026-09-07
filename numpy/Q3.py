import numpy as np

a = np.arange(1, 13).reshape(3, 4)
a[1:, 1:3] = 0
#print(a)


a = np.arange(20)
#print(a[2:15:3])


a = np.array([4,5,2])

#print(a [ a >= 4])


a = np.array(
    [
        [1, 2, 3],
        [4, 5, 6]
    ])
#print(a.sum(axis=0))
#print(a.sum(axis=1))

a = np.arange(12).reshape(3,4)

print(a[:,1])