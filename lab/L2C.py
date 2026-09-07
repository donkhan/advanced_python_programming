import numpy as np


a = np.arange(6)
b = np.arange(2,8,1)

print(a)
print(b)

print(a.shape)
print(b.shape)

print(a + b)
#print(a - b)
#print(a * b)
#print(a / b)


print(a.reshape(2,3) * b.reshape(2,3))

