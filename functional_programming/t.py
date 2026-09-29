from itertools import *
from functools import *

l = [ 3,4,5,12,6,7]

r = reduce(lambda x, y : x if x > y else y , l)
print(r)