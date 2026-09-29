from itertools import *
from functools import *


# Sum of numbers who are more than the average of the given numbers
numbers = [3, 7, 2, 8, 5, 10, 4, 9]
print(reduce(lambda x, y: x + y, filter(lambda x: x > reduce(lambda x, y: x + y, numbers) / len(numbers), numbers)))

# First number which crosses 15
numbers = [12, 5, 8, 21, 4, 17, 10, 3]
print(next(dropwhile(lambda x: x < 15,numbers)))

# Pairwise - from 3.10 only
numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17]
#print(next(dropwhile(lambda t: t[0] + t[1] < 25, pairwise(numbers))))


# No of elements in a list
numbers = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]
print(reduce(lambda x, y: x + 1, numbers, 0))

# No of elements in each group
print(
list(
    map(
        lambda g: reduce(lambda x, y: x + 1, g[1], 0),
        groupby(numbers)
    )
)
)

numbers = [3, 5, 7, 2, 9, 4, 6]
print(list(zip(numbers,accumulate(numbers))))