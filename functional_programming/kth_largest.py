from functools import *

numbers = [12, 15, 7, 20, 9, 30, 11, 18]


def find_kth_largest(l, k):
    return reduce(lambda x, y: x if x > y else y, l) if k == 1 else find_kth_largest(list(filter(lambda x: x != reduce(lambda x, y: x if x > y else y, l), l)), k-1)


print(find_kth_largest(numbers, 5))


numbers = [3, 7, 2, 8, 5, 10, 4, 9]
# Find the sum of the numbers that are greater than the average of the list.
print(reduce(lambda x, y: x + y, filter(lambda x: x > reduce(lambda x, y: x + y, numbers) / len(numbers), numbers)))


