import itertools


def f(x):
    return x * 12


#print(list(map(f, [1, 2, 3])))
#print(list(map(lambda x: x + 2, [1, 2, 3])))
#print(list(itertools.accumulate([1, 2, 3])))
#print(list(itertools.product('ABCDEF', 'XY')))
#print(list(itertools.product('ABCDEF')))

#print(list(itertools.permutations(range(5), 3)))
#print(list(itertools.combinations(range(5), 3)))

#print(list(itertools.repeat("A", 2)))

a, b = itertools.tee(itertools.combinations(range(1,5), 2))
print(next(a))
print(next(b))


# Q1
a = [1, 2, 3, 4]
x = list(map(lambda n: n * n - 1, a))
y = list(itertools.accumulate(x, lambda p, q: p + 2*q))
#print(x)
#print(y)


# Q2
p = itertools.product([1, 2, 3], repeat=2)
#print(list(p))
result = list(
    map(
        lambda x: x[0] * 10 + x[1],
        filter(lambda x: x[0] != x[1], p)
    )
)
#print(result)

# Q3
p = itertools.permutations([1, 2, 3, 4], 2)
result = list(
    map(
        lambda x: x[0] * x[1],
        filter(lambda x: sum(x) % 2 == 1, p)
    )
)
#print(result)

# Q4
data = [1, 2, 3, 4]
a = list(itertools.accumulate(data, lambda x, y: x * y))
b = list(map(lambda x: x + 1, a))
#print(a)
#print(b)

# Q5
c = itertools.combinations([1, 2, 3, 4, 5], 3)
result = list(
    map(
        lambda x: sum(x),
        filter(lambda x: sum(x) > 8, c)
    )
)
#print(result)

# Q6
a = [1, 2, 3, 4]
b = itertools.repeat(10, 4)
result = list(
    map(
        lambda x: x[0] * x[1] + 1,
        zip(a, b)
    )
)
#print(result)


# Q7
p = itertools.product([1, 2, 3], repeat=2)
x = map(
    lambda t: t[0] * t[1],
    filter(lambda t: sum(t) % 2 == 0, p)
)
result = list(
    itertools.accumulate(x, lambda a, b: a + b)
)
print(result)

# Q8
data = [1, 2, 3, 4]
result = list(
    itertools.accumulate(
        map(
            lambda x: x[0] + x[1],
            itertools.combinations(data, 2)
        ),
        lambda a, b: a * b
    )
)
print(result)

# Q9
a = [1, 2, 3, 4, 5]
result = list(
    map(
        lambda x, y: x ** y,
        a,
        itertools.repeat(2)
    )
)
print(result)

# Q10

p = itertools.product([1, 2, 3], repeat=2)


result = list(
    itertools.accumulate(
        map(
            lambda x: x[0] - x[1],
            filter(
                lambda x: x[0] + x[1] > 3,
                p
            )
        ),
        lambda a, b: a + b
    )
)
print(result)

# Q11
# Permutations would give AB,AC,AD,BA,BC,BD,CA,CB,CD,DA,DB,DC
# Combinations would give AB,AC,AD,BC,BD,CD
# Map would give ABAB,ACAC,ADAD,BABC, BCBD, BDCD
a = itertools.permutations("ABCD", 2)
b = itertools.combinations("ABCD", 2)
result = list(
    map(
        lambda x, y: x + y,
        a,
        b
    )
)
print(result)


# Q12
p = itertools.permutations([1, 2, 3], 2)
print(next(p))
print(next(p))
x = list(p)
print(x)

# Q13
p = itertools.permutations([1, 2, 3], 2)
first = next(p)
result = list(
    map(
        lambda x, y: x[0] + x[1] + y,
        p,
        itertools.repeat(10, 3)
    )
)
print(first)
print(result)

# Q14
p = itertools.product(range(1, 4), repeat=2)
result = list(
    itertools.accumulate(
        map(
            lambda x: x[0] * x[1],
            filter(
                lambda x: x[0] != x[1] and sum(x) > 3,
                p
            )
        ),
        lambda a, b: a - b
    )
)
print(result)


# Q15
p = itertools.permutations([1, 2, 3], 2)
a = list(filter(lambda x: x[0] < x[1], p))
b = list(map(lambda x: x[0] * 10 + x[1], p))
print(a)
print(b)


# Q17
p = itertools.permutations([1, 2, 3], 2)
a = list(map(lambda x: x[0] + x[1], p))
p = itertools.permutations([1, 2, 3], 2)
b = list(
    itertools.accumulate(
        filter(lambda x: x % 2 == 0, a),
        lambda x, y: x + y
    )
)
print(a)
print(b)

# Q18
p = itertools.permutations([1, 2, 3], 2)
x = next(p)
y = list(itertools.islice(p, 2))

z = list(
    map(
        lambda t: t[0] * 10 + t[1],
        p
    )
)

print(x)
print(y)
print(z)

# Q19
data = [2, 4, 6, 8, 9, 10, 12]
x = itertools.takewhile(
    lambda n: n % 2 == 0,
    data
)
print(list(x))
print(list(x))


# Q20
p = iter([10, 20, 30, 40, 50])
a, b = itertools.tee(p)

print(next(a))
print(next(a))
print(next(b))
print(list(a))
print(list(b))

# Q21
p = iter([2, 4, 6, 7, 8, 10])
a, b = itertools.tee(p)

x = list(itertools.takewhile(lambda n: n < 7, a))
y = list(b)

print(x)
print(y)

# Q22
p = iter([2, 4, 6, 7, 8, 10])
a, b = itertools.tee(p)
x = list(itertools.takewhile(lambda n: n < 7, a))
print(x)
print(next(a))
print(next(b))
print(next(b))


# Q23
p = itertools.count(1)
a, b = itertools.tee(p)
x = list(itertools.islice(a, 3))
y = list(
    itertools.accumulate(
        itertools.islice(b, 5),
        lambda x, y: x * y
    )
)
z = next(a)
print(x)
print(y)
print(z)


# Q24
p = itertools.count(1)
a, b = itertools.tee(p)
a = itertools.filterfalse(lambda x: x % 3 == 0, a)
x = list(itertools.islice(a, 5))
y = list(
    itertools.islice(
        map(lambda x: x * 2, b),
        7
    )
)
z = next(a)
print(x)
print(y)
print(z)


# Q25
p = iter([1, 2, 4, 6, 7, 8, 10, 12])
a, b = itertools.tee(p)
x = list(itertools.takewhile(lambda n: n < 7, a))
y = list(itertools.dropwhile(lambda n: n < 7, b))
print(x)
print(y)


# Q26
p = itertools.product(range(1, 4), repeat=2)
# (1,1)(1,2)(1,3)(2,1)(2,2)(2,3)(3,1)(3,2)(3,3)
# (1,2)(1,3)(2,1)(2,3)(3,1)(3,2)
# 1,1,2,8,3,9
result = list(
    itertools.starmap(
        lambda x, y: x ** y,
        filter(lambda t: t[0] != t[1], p)
    )
)
print(result)



# Q27
p = itertools.product(range(1, 4), repeat=2)
# (1,1)(1,2)(1,3)(2,1)(2,2)(2,3)(3,1)(3,2)(3,3)
a, b = itertools.tee(p)
# 2,3,4,3
x = list(itertools.starmap(
    lambda x, y: x + y,
    itertools.islice(a, 4)
))

#(1,1)(1,2)(1,3)(2,1)(2,2)(2,3)
# 1,2,3,2,4,6
y = list(itertools.starmap(
    lambda x, y: x * y,
    itertools.takewhile(lambda t: t[0] < 3, b)
))
z = list(a)
print(x)
print(y)
print(z)


# Q28
p = itertools.product(range(1, 4), repeat=2)

q = itertools.filterfalse(
    lambda t: t[0] + t[1] == 4,
    p
)
r = itertools.starmap(
    lambda x, y: x * y,
    q
)
print(next(r))
print(list(itertools.islice(r, 2)))
print(list(r))

# Q29
p = itertools.count(1)
a, b = itertools.tee(p)
x = list(itertools.islice(a, 3))
y = list(itertools.islice(
    filter(lambda n: n % 2 == 0, b),
    2
))
z = next(a)
print(x)
print(y)
print(z)


# Q30
p = itertools.count(1)
a, b = itertools.tee(p)
x = list(itertools.islice(
    itertools.filterfalse(lambda n: n % 2 == 0, a),
    3
))
y = list(itertools.islice(b, 5))
z = next(a)
print(x)
print(y)
print(z)


# Q31
data = [2, 3, 1, 4]
a, b = itertools.tee(data)
p = itertools.accumulate(a, lambda x, y: x ** y)
q = itertools.starmap(
    lambda x, y: x - y,
    zip(p, b)
)
result = list(q)
print(result)

# Q32
# Read Documentation

data = [
    ("A", 10),
    ("A", 20),
    ("B", 5),
    ("A", 30),
    ("B", 15),
    ("B", 25),
]
result = []
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    result.append((key, sum(x[1] for x in group)))
print(result)

# Q33

data = [1, 2, 3, 4, 5]
a = itertools.accumulate(data, lambda x, y: x + y)
b = itertools.islice(a, 2, 5)
c = map(lambda x: x * 2, b)
print(list(c))

# Q34
data = [1, 2, 3, 4]
a = itertools.accumulate(data, lambda x, y: x * y)
b = itertools.filterfalse(lambda x: x % 2 == 0, a)
print(list(b))

# Q35
data = [1, 2, 3, 4, 5, 6]
a, b = itertools.tee(data)
x = itertools.accumulate(a, lambda p, q: p + q)
y = itertools.islice(x, 1, None, 2)
z = itertools.starmap(
    lambda p, q: p * q,
    zip(y, b)
)
print(list(z))

# Q36
data = [1, 2, 1, 3, 2, 3]
a = itertools.accumulate(data, lambda x, y: x + y)
b = itertools.cycle([10, 20])
c = itertools.islice(b, 1, 7)
d = itertools.starmap(
    lambda x, y: x - y,
    zip(a, c)
)
e = itertools.filterfalse(
    lambda x: x < 0,
    d
)
print(list(e))

# Q37
data = [2, 1, 3, 2]
a = itertools.accumulate(data, lambda x, y: x * y)
b = itertools.tee(a, 2)
c = itertools.takewhile(lambda x: x < 7, b[0])
d = itertools.dropwhile(lambda x: x < 3, b[1])
e = itertools.zip_longest(c, d, fillvalue=0)
print(list(e))

# Q38

data = [1, 1, 2, 2, 3]
groups = itertools.groupby(data)
for key, group in groups:
    print(key, list(group))

# Q39

data = [1, 2, 3, 4, 5]
a = itertools.accumulate(data, lambda x, y: x + y)
b = itertools.takewhile(lambda x: x <= 6, a)
print(list(b))


# Q40
data = [1, 2, 3, 4, 5]
a = itertools.accumulate(data, lambda x, y: x * y)
b = itertools.islice(a, 1, 5, 2)
c = itertools.repeat(2)
d = itertools.starmap(
    lambda x, y: x + y,
    zip(b, c)
)
print(list(d))

# Q41
data = [10, 20, 30, 40, 50, 60]
a = itertools.islice(data, 1, 5, 2)
b = itertools.islice(data, 0, 6, 3)

print(list(a))
print(list(b))

# Q42
data = [10, 20, 30, 40, 50, 60, 70]
a = itertools.islice(data, 2, None, 2)
b = itertools.islice(reversed(data), 1, 5, 2)
print(list(a))
print(list(b))

# Q43
data = [1, 2, 3, 4]
a = itertools.accumulate(data, lambda x, y: x + y)
b = itertools.tee(a, 2)
c = itertools.takewhile(lambda x: x < 7, b[0])
d = itertools.dropwhile(lambda x: x < 3, b[1])

print(list(c))
print(list(d))

# Q44

data = [3, 1, 4, 2]


def f(x, y):
    if y % 2 == 0:
        return x * y
    return x + y


a = itertools.accumulate(data, f)
b = itertools.filterfalse(
    lambda x: x % 3 == 0,
    a
)
print(list(b))


# Q45
data = [2, 3, 1, 4]
a = itertools.accumulate(
    data,
    lambda x, y: x // y if x > y else x + y
)
b = itertools.tee(a, 2)
c = itertools.takewhile(lambda x: x < 10, b[0])
d = itertools.dropwhile(lambda x: x < 4, b[1])
e = itertools.zip_longest(c, d, fillvalue=0)
print(list(e))


# Q46
data = [1, 1, 2, 2, 2, 3, 1, 1]
g = itertools.groupby(data)
a = []
for key, group in g:
    if key % 2 == 0:
        a.append((key, sum(group)))
    # Try with removing else
    else:
        next(g, None)

# Q47
data = [2, 4, 1, 3]
a = itertools.accumulate(
    data,
    lambda x, y: x // y if x % y == 0 else x + y
)
b, c = itertools.tee(a)
d = itertools.dropwhile(lambda x: x < 4, b)
e = itertools.takewhile(lambda x: x <= 6, c)
print(list(d))
print(list(e))


# Q48
data = [1, 2, 2, 3, 3, 3, 4]
g = itertools.groupby(data)
result = []
for key, group in g:
    values = list(group)
    if len(values) > 1:
        result.append((key, len(values)))
print(result)

# Q49
data = [1, 1, 2, 2, 3, 3]
g = itertools.groupby(data)
first = next(g)
second = next(g)
print(first[0], list(first[1]))
print(second[0], list(second[1]))

# Q50
data = [1, 2, 3, 4, 5]
a = itertools.filterfalse(lambda x: x % 2, data)
b = itertools.accumulate(a, lambda x,y: x + y)
print(list(b))

# Q51
data = [1, 2, 3, 4, 5, 6]
a = itertools.filterfalse(lambda x: x % 2, data)
b = itertools.accumulate(a, lambda x, y: x * y)
c = itertools.filterfalse(lambda x: x > 10, b)
print(list(c))


# Q52
data = [10, 20, 30, 40, 50, 60]
selectors = [1, 0, 1, 1, 0, 0]
a = itertools.compress(data, selectors)
b = itertools.accumulate(a, lambda x, y: x + y)
print(list(b))

# Q53
data = [2, 4, 6, 8, 10]
selectors = [1, 0, 1, 1, 0]
a = itertools.compress(data, selectors)
b, c = itertools.tee(a)
d = itertools.accumulate(b, lambda x, y: x + y)
e = itertools.starmap(
    lambda x, y: x * y,
    zip(c, d)
)
print(list(e))

# Q54
data = iter([1, 2, 3, 4])
a, b = itertools.tee(data)
x = itertools.chain(
    itertools.islice(a, 0, 2),
    b
)
y = itertools.chain(
    itertools.islice(a, 2, 4),
    x
)
print(list(y))


# Q58
data = iter([1, 2, 3])
a, b = itertools.tee(data)
x = itertools.chain(
    a,
    b
)
print(list(x))


# Q59
data = iter([1, 2, 3, 4])
a, b = itertools.tee(data)
x = itertools.chain(
    filter(lambda n: n % 2 == 0, a),
    b
)
print(list(x))


# Q60
data = iter([1, 2, 3, 4])
a, b = itertools.tee(data)
x = itertools.chain(
    filter(lambda n: n % 2 == 0, a),
    b
)
y = itertools.chain(
    x,
    filter(lambda n: n > 2, b)
)
print(list(y))


# Q61 A committee of 5 people is to be selected from:
# 7 men and 5 women. The committee must contain at least 2 women.
students = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
students_with_both_a_and_b_present = list(itertools.combinations(students, 4))
c = 0
for i in students_with_both_a_and_b_present:
    x = list(i)
    if 'A' in x and 'B' in x:
        pass
    else:
        c = c + 1
print(c)

# Pythonic Version
print(len([x for x in itertools.combinations(students,4) if not('A' in x and 'B' in x)]))


# Q62
digits = [1, 2, 3, 4, 5, 6]
print([str(x[0])+str(x[1])+str(x[2])+str(x[3]) for x in itertools.permutations(digits,4) if x[3] % 2 == 0
      and '12' not in str(x[0])+str(x[1])+str(x[2])+str(x[3]) and '21' not in str(x[0])+str(x[1])+str(x[2])+str(x[3])])
# Pythonic Version
print( [
    x for x in itertools.permutations(digits, 4)
    if x[3] % 2 == 0
    and all(
        not ({x[i], x[i+1]} == {1, 2})
        for i in range(3)
    )
])


# Q63 In plain English, what does this condition mean?
data = [1, 2, 3, 4]
print([
    x for x in itertools.permutations(data, 3) if any(n == 4 for n in x)
])

# Q64
# Generate all 3-digit numbers without repetition such that:
# the number contains at least one even digit
# the number contains at least one odd digit
digits = [1, 2, 3, 4]
print([
    x for x in itertools.permutations(digits, 3) if any(n % 2 == 0 for n in x) and any(n % 2 == 1 for n in x)
])

# Q65
# Generate all 4-digit numbers without repetition such that:
# The number is even.
# Exactly two digits are odd.
# 1 and 2 are not adjacent.
# and all(
#         not ({x[i], x[i+1]} == {1, 2})
#         for i in range(3)
#     )
print("Q65")
digits = [1, 2, 3, 4, 5, 6]
print(
    [x for x in itertools.permutations(digits, 4)
     if x[3] % 2 == 0
        and
     all(
        not ({x[i], x[i+1]} == {1,2}) for i in range(3)
    )
         and
    sum(n % 2 == 1 for n in x) == 2
]
)

# Q66 Generate all 4-digit numbers without repetition such that:
# exactly two digits are even
# the first digit is smaller than the last digit
# 2 and 5 cannot appear together
digits = [1, 2, 3, 4, 5, 6]
print([x for x in itertools.permutations(digits,4) if sum(n%2 == 0 for n in x) == 2 and x[0] < x[3] and all(not ({x[i],x[i+1]} == {2,5}) for i in range(3))])

# Q67 Generate all 4-digit numbers without repetition such that:
#
# exactly two digits are odd
# the number contains 3
# 3 is not in the first or last position
# the two odd digits are not adjacent

digits = [1, 2, 3, 4, 5]
print([x for x in itertools.permutations(digits,4) if x[0] != 3 and x[3] != 3 and sum(n % 2 == 1 for n in x) == 2 and
    sum(n == 3 for n in x) > 0 and  sum({x[i] % 2, x[i+1] % 2} == {1,1} for i in range(3)) == 0])


# Q68 Cycle What is the output, and why?
x = itertools.cycle([1, 2, 3])
for i in range(8):
    print(next(x), end=" ")

# Q69
x = itertools.cycle([10, 20, 30])
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Q70
x = itertools.cycle([1, 2, 3])
print(next(x))
print(next(x))
y = next(x)
print(y)
print(next(x))

# Q71
x = itertools.cycle([1, 2, 3])
a = next(x)
b = next(x)
print(a, b)
for _ in range(4):
    print(next(x), end=" ")


# Q72
x = itertools.cycle([1, 2, 3])
a = [next(x) for _ in range(4)]
y = [next(x) for _ in range(5)]
print(a)
print(y)


# Q73
x = itertools.cycle([1, 2, 3])
a = next(x)
b = [next(x) for _ in range(3)]
c = next(x)
print(a)
print(b)
print(c)

# Q74
x = itertools.cycle([1, 2, 3])
y = x
print(next(x))
print(next(y))
print(next(x))
print(next(y))

# Q75
x = itertools.cycle([1, 2, 3])
y = itertools.cycle(x)
print(next(x))
print(next(y))
print(next(y))
print(next(x))

# Q76
faculty = ["Kamil", "Anita", "Ravi"]
i = itertools.cycle(faculty)
c = 1
for ix in range(1, 12):
    f = next(i)
    if c == 7 and f == 'Kamil':
        continue
    print(c, f, end=" ")
    c = c + 1

print()
# Q77 But there are two rules:
# Ravi is unavailable on days 5, 6, and 7.
# Whenever a faculty member is unavailable, the next available faculty member takes that day.
# The rotation should continue from where it left off — an unavailable faculty member should not permanently disappear
# from the rotation.

faculty = ["Kamil", "Anita", "Ravi"]
i = itertools.cycle(faculty)
days = range(1, 16)
for day in days:
    f = next(i)
    while (day == 5 or day == 6 or day == 7) and f == 'Ravi':
        f = next(i)
    print(day, f)

# Q78
# Generate assignments for 20 consecutive sessions.
# Rules:
# Faculty rotate continuously.
# Tasks rotate continuously.
# Ravi cannot handle MongoDB.
# Anita cannot handle PowerBI.
# When a faculty member cannot handle the current task, advance the faculty rotation until someone can.
# The task rotation must NOT advance because of a faculty rejection.
faculty = ["Kamil", "Anita", "Ravi"]
tasks = ["Cloud", "Python", "MongoDB", "PowerBI"]
f_c = itertools.cycle(faculty)
t_c = itertools.cycle(tasks)
for a in range(1,21):
    f = next(f_c)
    t = next(t_c)
    if f == 'Ravi' and t == 'MongoDB':
        f = next(f_c)
    if f == 'Anita' and t == 'PowerBI':
        f = next(f_c)
    print(f,t)
