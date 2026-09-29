from functools import *

numbers = [12, 15, 7, 20, 9, 30, 11, 18]


def find_kth_largest_iterative(_numbers, k):
    if k > len(_numbers):
        return None
    for i in range(1, k+1):
        _max = _numbers[0]
        # Find Maximum
        for j in range(0, len(_numbers)):
            if _max < _numbers[j]:
                _max = _numbers[j]
        # Remove Max if it is not kth iteration
        if i < k:
            _numbers.remove(_max)
    return _max


def find_kth_largest(l, k):
    return None if k > len(l) else reduce(lambda x, y: x if x > y else y, l) if k == 1 else \
        find_kth_largest(list(filter(lambda x: x != reduce(lambda x, y: x if x > y else y, l), l)), k-1)


print(find_kth_largest(numbers, 3))
print(find_kth_largest_iterative(numbers, 3))

