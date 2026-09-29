from itertools import *
from functools import *

numbers = [12, 15, 7, 20, 9, 30, 11, 18]


def find_kth_largest(l, k):
    return reduce(lambda x, y: x if x > y else y, l) if k == 1 else find_kth_largest(list(filter(lambda x: x !=
                                                    reduce(lambda x, y: x if x > y else y, l), l)), k-1)


#print(find_kth_largest(numbers, 5))

numbers = [3, 7, 2, 8, 5, 10, 4, 9]
#print(reduce(lambda x, y: x + y, filter(lambda x: x > reduce(lambda x, y: x + y, numbers) / len(numbers), numbers)))

numbers = [12, 5, 8, 21, 4, 17, 10, 3]
#print(next(dropwhile(lambda x: x < 15,numbers)))

numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17]
#print(next(dropwhile(lambda t: t[0] + t[1] < 25, pairwise(numbers))))


numbers = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]
print(reduce(lambda x, y: x + 1, numbers, 0))

print(
list(
    map(
        lambda g: reduce(lambda x, y: x + 1, g[1], 0),
        groupby(numbers)
    )
)
)