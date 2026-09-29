from itertools import *
from functools import *


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

z = zip(numbers, accumulate(numbers))
print(next(dropwhile(lambda a: a[1] < 15, z))[0])