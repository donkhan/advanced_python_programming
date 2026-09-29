from itertools import *
from functools import *

l = [3, 4, 5, 12, 6, 7]
r = reduce(lambda x, y : x if x > y else y , l)
# print(r)

# Instead of a running sum, produce a running maximum:
numbers = [3, 7, 2, 9, 4, 8]
# print(list(accumulate(numbers, lambda x, y: x if x > y else y)))

# Produce the elements that are new maximums as the sequence progresses.
numbers = [3, 7, 2, 9, 4, 8, 6, 11, 5]
# print(list(map(lambda t: t[0], groupby(accumulate(numbers, lambda x, y: x if x > y else y)))))

numbers = [4, 6, 3, 8, 8, 2, 10, 7, 12, 12, 5]

print(list(accumulate(numbers, lambda x, y: x if x > y else y)))
print(list(map(lambda t: t[0] if t[0] == t[1] else 0, zip(numbers, accumulate(numbers, lambda x, y: x if x > y else y)))))

numbers = [4, 7, 2, 9, 5, 11, 3, 8]
m = map(lambda t: t[1] - t[0], zip(numbers, accumulate(numbers, lambda x, y: x if x > y else y)))
print(list(m))