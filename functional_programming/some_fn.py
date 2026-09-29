
from functools import *


# print(reduce(lambda x, y: x*y, range(1, int(input("Enter the No ")) + 1)))
# print(reduce(lambda x, y: x+y, range(1, int(input("Enter the No ")) + 1)))
# print(reduce(lambda x, y: x*y, filter(lambda  n: n%2 == 0, range(1,11))))
# print(reduce(lambda x, y: x if x > y else y, [1,2,4,5,6,34,12]))
# print(reduce(lambda x, y: x + y, map(lambda  x: x*x, filter(lambda x: x % 2 == 1, [12, 7, 15, 8, 21, 10, 6]))))
# print(reduce(lambda x, y: x * y, filter(lambda x: x > 16, [4, 9, 16, 25, 36, 49])))

# reduce(lambda  x,y: x*y, filter(lambda x: x % 2 != 0 and x % 3 == 0, [12, 5, 8, 21, 30, 17, 4, 9]))
from itertools import repeat

numbers = [12, 15, 7, 20, 9, 30, 11, 18]
#print(reduce(lambda x, y: x if x > y else y, filter(lambda x: x != reduce(lambda x, y: x if x > y else y,
#                                    [12, 15, 7, 20, 9, 30, 11, 18]), [12, 15, 7, 20, 9, 30, 11, 18])))


def a(t, n):
    if len(t) == 0:
        return n,
    if len(t) == 1:
        if n > t[0]:
            return n, t[0]
        else:
            return t[0], n
    if n > t[0]:
        return n, t[0]
    if n > t[1]:
        return n, t[1]
    return t


# print(reduce(lambda x, y: a(x, y), numbers, ())[1])
# print(reduce(lambda x, y: x*y, map(lambda x: x**3, filter(lambda x: x % 5 == 0, [1,4,5]))))

numbers = [12, 5, 18, 7, 24, 9, 30, 11, 16]

r1 = reduce(lambda x, y: x if x > y else y, filter(lambda x: x % 2 == 0, numbers))
m = reduce(lambda x, y: x if x > y else y, filter(lambda x: x % 2 == 0 and x != r1, numbers)) + r1
# print(m)

# kth largest

def remove_largest(numbers):
    return list(filter(lambda x: x != reduce(lambda x, y: x if x > y else y, numbers), numbers))


def compose(f, g):
    return lambda x: f(g(x))


remove_k_minus_1 = reduce(
    compose,
    repeat(remove_largest, 4)
)
print(reduce(lambda x, y: x if x > y else y, remove_k_minus_1(numbers)))

