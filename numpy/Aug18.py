import numpy

a = numpy.array([[2, 4, 6], [1, 3, 5], [8, 10, 12]])

a = numpy.array([[4, 8, 12],
              [16, 20, 24],
              [28, 32, 36]])

print(np.argmax(np.sum(a, axis=1)) + 1)
