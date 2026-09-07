import numpy as np

a = np.arange(1,50,2)
a = a.reshape(5,5)

print(a)

#print(a[(1,3), :])
#print(a[:, (1,-1)])
print(a[::-1,::-1])