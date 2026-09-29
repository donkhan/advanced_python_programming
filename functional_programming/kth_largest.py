from functools import *

numbers = [12, 15, 7, 20, 9, 30, 11, 18]


def find_kth_largest(l, k):
    return None if k > len(l) else reduce(lambda x, y: x if x > y else y, l) if k == 1 else find_kth_largest(list(filter(lambda x: x !=
                    reduce(lambda x, y: x if x > y else y, l), l)), k-1)


print(find_kth_largest(numbers, len(numbers)))

