import itertools

# Example 1


def f(x):
    return x * 2


def g(x):
    return x + 3


def h(x):
    return x ** 2


data = [1, 2, 3, 4]

result = list(
    # 25,49,81,121
    map(
        h,
        # 5,7,9,11
        map(
            g,
            # 2,4,6,8
            map(f, data)
        )
    )
)

print(result)

# C2


def compose(f, g):
    return lambda x: f(g(x))


c = compose(h, compose(g, f))

print(c(2))
print(c(5))

# C3
c1 = compose(g, f)
c2 = compose(h, c1)
print(c1(4))
print(c2(4))

# C4
c = compose(g, h)
result = list(map(c, [1, 2, 3, 4]))
print(result)

# C5
c = compose(h, f)
result = list(
    map(
        g,
        filter(lambda x: c(x) > 20, [1, 2, 3, 4, 5])
    )
)
print(result)

# C6
c1 = compose(g, f)
c2 = compose(h, c1)
result = list(
    map(c2, filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
)

print(result)

# C7


def apply_twice(fn):
    return lambda x: fn(fn(x))


c = compose(g, f)
d = apply_twice(c)
result = list(
    map(
        h,
        filter(
            lambda x: d(x) % 3 == 0,
            range(1, 8)
        )
    )
)
print(result)


# C8
from functools import reduce

c = compose(g, f)

result = reduce(
    lambda acc, x: c(acc) + h(x),
    [1, 2, 3],
    0
)

print(result)


# C9
c = compose(g, f)

data = [1, 2, 3, 4]

result = reduce(
    lambda a, b: c(a) + b,
    map(h, data)
)

print(result)

# C10
c = compose(g, f)
data = [1, 2]
result = reduce(
    lambda a, b: c(a) if b % 2 else h(b),
    data,
    1
)
print(result)

# C11
c = compose(g, f)
data = [1, 2, 3, 4]
result = reduce(
    lambda a, b: c(b) - a,
    data,
    0
)
print(result)

# C12
c = compose(g, f)
data = [1, 2, 3, 4]
mapped = map(c, data)
result = reduce(
    lambda a, b: a * b,
    mapped,
    1
)

print(result)

# C13


def apply(fn, x):
    return fn(x)


c1 = compose(g, f)
c2 = compose(h, c1)
functions = [f, g, c1, c2]
result = list(
    map(
        lambda fn: apply(fn, 2),
        functions
    )
)

print(result)

# C14


def make(n):
    return lambda fn: fn(n)


c = compose(g, f)
functions = [f, g, c, h]
result = list(
    map(make(3), functions)
)

print(result)


# C15
def twice(fn):
    return lambda x: fn(fn(x))


functions = [f, g, h]
result = list(
    map(
        lambda fn: fn(2),
        map(twice, functions)
    )
)

print(result)


# C16
def twice(fn):
    return lambda x: fn(fn(x))


c = compose(g, f)
p = twice(c)
result = list(map(p, [1, 2, 3]))
print(result)


# C17
def twice(fn):
    return lambda x: fn(fn(x))


c = compose(g, f)
p = twice(c)

data = [1, 2, 3, 4, 5]
result = list(
    map(p, filter(lambda x: x % 2 == 0, data))
)
print(result)


# C19
def twice(fn):
    return lambda x: fn(fn(x))


c = compose(g, f)
p = twice(c)

data = [1, 2, 3, 4]
result = list(
    map(
        lambda x: p(x) - c(x),
        data
    )
)
print(result)


# C21
def add(n):
    return lambda x: x + n


def multiply(n):
    return lambda x: x * n


c = compose(
    add(3),
    multiply(2)
)
result = list(map(c, [1, 2, 3, 4]))
print(result)


# C22
add5 = add(5)
double = multiply(2)
c = compose(add5, double)
print(c(10))


# C23
def add(n):
    return lambda x: x + n

def multiply(n):
    return lambda x: x * n

functions = [
    add(2),
    multiply(3),
    add(4)
]

c = compose(functions[0], compose(functions[1], functions[2]))

print(c(5))