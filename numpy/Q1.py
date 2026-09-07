import numpy as np
import numpy.char as c


_array = np.array([[1, 2, 3], [4, 5, 6]])
a = _array

print(np.argmax(a))
print(np.argmin(a))



print(_array.shape)
print(_array)
_x = np.reshape(_array, (3, 2))


print(_x)
print(_x.shape)

print(np.log(3))

print(np.log10(20))

c = np.array(['aAaAaA', '  aA  ', 'abBABba'])

c = np.strings.strip(c)
print(c)

print(np.char.lower(c))

