import numpy as np
import pandas as pd
from itertools import *
from functools import *

# 1
a = np.array([2, 4, 6, 8])
b = a[1:3]
b *= 10
print(a)
print(b)

# 2
df = pd.DataFrame({
    "dept": ["CS", "AI", "CS", "AI"],
    "marks": [70, 80, 90, 60]
})
result = df.groupby("dept")["marks"].mean()
print(result["CS"])
print(result["AI"])

# 3
x = [2, 3, 4]
result = list(accumulate(x, lambda a, b: a * b))
print(result)


# 4
x = [1, 2, 3, 4]
y = list(accumulate(x, lambda a, b: a + 2*b))
print(y)

# 5
x = [2, 3, 4, 5]
r = reduce(lambda a, b: a + b if b % 2 else a * b, x, 1)



# 6
x = [2, 4, 6, 8]
y = x[1:]
y[1] = 99

print(x)
print(y)



# 7
x = [2, 4, 6, 8]
y = x[1:]
y[1] = 99
print(x)
print(y)

# 8
x = [1, 2, 3, 4, 5]
y = list(map(lambda n: n * 2, filter(lambda n: n % 2, x)))
print("Q8")
print(y)


# 9
x = [1, 2, 3, 4]
y = list(map(lambda n: n + 1, x))
x[1:3] = y[2:4]
print("Q9")
print(x)
print(y)


# 10
x = [1, 2, 3, 4, 5]
y = list(filter(lambda n: n > 2, map(lambda n: n * 2 - 1, x)))
print("Q10")
print(y)



# 11
x = [2, 4, 6, 8]
y = x
x = x + [10]
y.append(12)
print("Q11")
print(x)
print(y)



# 12
x = [1,2,3,4,5]
a = list(map(lambda n:n*2,x))
b = list(filter(lambda n:n%3==0,a))
x[2] = 10
print("Q12")
print(a)
print(b)
print(x)

# 13
x = [1,2,3,4]
y = map(lambda n:n*2,x)
x[1] = 10
print(list(y))


# 14
x = [1,2,3,4]
y = filter(lambda n:n%2==0,x)
x.append(6)
print(list(y))


# 15
x = [1,2,3]
y = [10,20,30]
z = zip(x,y)
x.append(4)
print("Q15")
print(list(z))


# 16
x = [1,2,3]
y = iter(x)
x.append(4)
print("Q16")
print(next(y))
print(next(y))
print(list(y))


# 17
x = [1,2,3,4]
y = iter(x)
print(next(y))
x[1] = 20
print(list(y))

# 18
x = [1,2,3,4]
y = iter(x)
print(next(y))
x[1] = 20
print(list(y))

# 19
x = [1,2,3,4]
y = list(map(lambda n:n+1,x))
z = filter(lambda n:n%2==0,y)
x[0] = 10
print("Q19")
print(list(z))
print(y)



# 20
x = [1,2,3,4]
y = map(lambda n:n*2,x)
z = map(lambda n:n+1,y)
x[2] = 10
print(list(z))

# 21
x = [1,2,3,4]
y = list(map(lambda n:n*2,x))
x[:] = y
y[1] = 99
print("Q21")
print(x)
print(y)



# 22
x = [1,2,3,4]
y = iter(x)
x.reverse()
print("Q22")
print(next(y))
print(list(y))


# 23
a = np.array([2,4,6,8,10])
b = a[1:4]
b += 5
print(a)
print(b)

# 24
df = pd.DataFrame({"dept":["CS","AI","CS","AI"],"marks":[60,80,90,70]})
x = df.groupby("dept")["marks"].sum()
df.loc[0,"marks"] = 100
print(x["CS"])
print(df["marks"].sum())

# 25
a = np.array([[1,2,3],[4,5,6]])
b = a[:,1]
b[:] = b * 10
print(a)
print(b)

# 26
df = pd.DataFrame({"A":[10,20,30,40],"B":[1,2,3,4]})
df.loc[df["A"] > 15,"B"] *= 10
print(df["B"].tolist())
print("Q26")


# 27
x = [2,3,4,5]
r = reduce(lambda a,b:a-b if b%2 else a+b,x,10)
print(r)
print("Q27")



# 28
a = np.array([1,2,3,4,5])
b = a[a % 2 == 1]
b *= 10
print(a)
print(b)
print("Q28")


# 29
x = [1,2,3,4]
y = accumulate(x,lambda a,b:a+b)
print(list(y))
print(list(y))
print("Q29")


# 30
a = np.array([[1,2,3],[4,5,6]])
b = a[:,1:]
b[0,0] = 99
print("Q30")
print(a)
print(b)



# 31
x = [1,2,3,4]
y = list(accumulate(x,lambda a,b:a*b))
z = reduce(lambda a,b:a+b,y,0)
print(y)
print(z)


# 32
df = pd.DataFrame({"A":[1,2,3,4],"B":[10,20,30,40]})
x = df.groupby(df["A"] % 2)["B"].sum()
print(x[0])
print(x[1])



# 33
x = [1,2,3,4]
y = accumulate(x,lambda a,b:a-b)
print(list(y))

# 34
a = np.array([1,2,3,4,5,6])
b = a[a > 2]
a[3:] = 0
print(a)
print(b)


# 35
df = pd.DataFrame({"A":[1,2,3,4],"B":[10,20,30,40]})
x = df["B"].map(lambda n:n//10)
y = x[x%2==0]
print(x.tolist())
print(y.tolist())

# 36
a = np.array([1,2,3,4])
b = a[1:3]
c = list(map(lambda x:x*2,b))
b[0] = 10
print(a)
print(c)

# 37
a = np.array([1,2,3,4])
b = a[1:3]
c = list(map(lambda x:x*2,b))
b[0] = 10
print(a)
print(c)


# 38
df = pd.DataFrame({"A":[1,2,3,4,5],"B":[10,20,30,40,50]})
x = df.loc[df["A"]>2,"B"]
x = x * 2
df.loc[3,"B"] = 100
print("Q38")
print(x.tolist())
print(df["B"].tolist())


# 39
x = [1,2,3,4]
y = list(map(lambda n:n+1,x))
z = list(filter(lambda n:n%2==0,y))
x[0] = 10
print(y)
print(z)

# 40
a = np.array([1,2,3,4,5])
b = a[::2]
c = b * 10
b[1] = 99
print(a)
print(c)

# 41
df = pd.DataFrame({"A":[1,2,3,4],"B":[10,20,30,40]})
x = df.groupby(df["A"]%2)["B"].mean()
df.loc[0,"B"] = 100
print(x.tolist())
print(df["B"].sum())


# 42
x = [1,2,3,4,5]
f = lambda n:n*2
g = lambda n:n+3
y = list(map(g,map(f,filter(lambda n:n%2,x))))
print(y)
exit(1)

# 43
x = [1,2,3,4,5,6]
f = lambda a,b:a+b if b%2 else a*b
r = reduce(f,x,1)
print(r)

# 44
x = [1,2,3,4,5]
f = lambda n:n*n
g = lambda n:n-1
y = list(map(g,filter(lambda n:n>10,map(f,x))))
print(y)

# 45
# Show Documentation
x = [1,2,3,4]
y = list(map(lambda a,b:a+b, x, x[1:]))
print(y)

# 46
x = [1,2,3,4]
y = list(map(lambda a,b:a*b, x, x[::-1]))
z = reduce(lambda a,b:a+b,y)
print(y)
print(z)

# 47
A = np.array([[1,2],[3,4]])
B = np.array([[2,0],[1,2]])
C = A @ B
print(C)

# 48
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,2],[3,4],[5,6]])
C = A @ B
print(C)

# 49
A = np.array([[1,2,3],[2,4,6],[1,1,1]])
print(np.linalg.matrix_rank(A))

# 50
A = np.array([[1,2,3],[2,4,6],[3,6,9]])
B = np.array([[1,2,3],[2,4,7],[3,6,10]])
print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(B))

# 51
A = np.array([[4,1],[2,3]])
print(np.linalg.eigvals(A))

# 52
x = [1, 2, 3, 4, 5]
y = list(filter(lambda n: n % 2 == 1, x))
z = list(map(lambda n: n * 2, y))
r = reduce(lambda a, b: a - b if a > b else a + b, z, 10)
print(y)
print(z)
print(r)


# 52
x = [1, 2, 3, 4, 5, 6]
y = list(map(lambda n: n + 1, filter(lambda n: n % 2 == 0, x)))
z = reduce(lambda a, b: a * 2 + b, y, 0)
print(y)
print(z)

# 53
x = [1, 2, 3, 4, 5]
y = list(map(lambda n: n * n, filter(lambda n: n % 2 == 1, x)))
z = reduce(lambda a, b: a + b if b % 3 else a * b, y, 2)
print(y)
print(z)

# 54
p1 = np.poly1d([1, 2, 3])
p2 = np.poly1d([9, 5, 1])
print(p1)
print(p2)
print(np.polymul(p1, p2))

# 55
print(np.polyder(p1))
print(np.polyint(p1))


# Q66
a = np.array([2, 5, 8, 5, 10])
b = np.array([3, 5, 7, 6, 10])
x = a <= b
y = a != b
print(x)
print(y)
print(a[x])

# Q67
a = np.array([4, 7, 10, 13, 16, 19])
b = (a > 6) & (a <= 16)
c = a[b]
d = a[a % 2 == 0]
print(b)
print(c)
print(d)

# Q68
a = np.array([3, 6, 9, 12, 15, 18])
x = (a > 5) & (a < 16)
y = ~x
print(x)
print(y)
print(a[y])

# 69
a = np.array([2, 5, 8, 11, 14, 17])
x = (a < 6) | (a >= 14)
y = a[x]
print(x)
print(y)

# 70
a = np.array([2, 5, 8, 11, 14, 17, 20])
x = ((a > 5) & (a < 18)) | (a == 2)
y = ~x
print(x)
print(y)
print(a[y])

# 71
a = np.array([1, 2, 3, 4, 5])
f = lambda x: x * 2
g = lambda x: x + 1
y = list(map(g, filter(lambda x: x > 4, map(f, a))))
print(y)

# 72
x = [1, 1, 2, 2, 2, 3, 1, 1]
y = [(k, list(g)) for k, g in groupby(x)]
z = list(map(lambda p: (p[0], len(p[1])), y))
print(y)
print(z)

# 73
x = [2, 4, 6]
c = cycle(x)
y = list(islice(c, 8))
z = list(filter(lambda n: n % 4 == 0, y))
w = list(map(lambda n: n // 2, z))
print(y)
print(z)
print(w)

# 74
x = [2, 3, 1, 4, 2]
y = list(accumulate(x, lambda a, b: a * b))
z = list(filter(lambda n: n % 3 == 0, y))
print(y)
print(z)

# 75
x = [2, 1, 3, 2, 4]
y = list(accumulate(x, lambda a, b: a + 2*b))
z = list(filter(lambda n: n % 3 != 0, y))
w = list(map(lambda n: n // 2, z))
r = reduce(lambda a, b: a - b if a > b else a + b, w, 20)
print(y)
print(z)
print(w)
print(r)


# 76
a = np.array([[2, 5, 8], [10, 3, 6], [7, 9, 4]])
x = a > 5
print(x)
print(np.all(x, axis=0))
print(np.any(x, axis=1))

# 77
a = np.array([[2, 4, 6], [7, 9, 11], [3, 8, 12], [5, 10, 15]])
x = a > 5
y = np.all(x, axis=1)
z = np.any(x, axis=1)
print(y)
print(z)
print(a[y])

# 78
a = np.array([3, 8, 5, 12, 7, 15])
x = np.where(a % 2 == 0, a * 2, a + 10)
y = x[x > 15]
print(x)
print(y)

# 79
a = np.array([[2, 8, 5], [10, 12, 3], [7, 4, 9], [14, 6, 11]])
x = np.all(a > 5, axis=1)
y = np.where(x, a[:, 0], -1)
print(x)
print(y)

# 80
x = [1, 2, 3, 4, 5, 6]
y = list(map(lambda n: n * 2, filter(lambda n: n % 2 == 0, x)))
z = list(map(lambda n: n - 1, y))
r = reduce(lambda a, b: a * b - a, z, 2)
print(y)
print(z)
print(r)

# 81
x = [1, 2, 3, 4, 5]
y = list(map(lambda n: n + 2, x))
z = list(filter(lambda n: n % 2 == 0, y))
r = reduce(lambda a, b: a * 2 + b, z, 1)
print(y)
print(z)
print(r)

# 83
x = [1, 2, 3, 4, 5]
y = list(accumulate(x, lambda a, b: a * 2 - b, initial=3))
print(y)

# 84
x = [2, 3, 1, 4]
y = list(accumulate(x, lambda a, b: a + b * 2, initial=1))
z = list(filter(lambda n: n % 2 == 0, y))
r = reduce(lambda a, b: a // 2 + b, z, 10)
print(y)
print(z)
print(r)

# 85
x = 0
for i in range(1, 6):
    if i % 2 == 0:
        x += i
    else:
        x -= i
print(x)

# 86
x = 1
i = 1
while i <= 5:
    if i % 2 == 0:
        x *= i
    else:
        x += i
    i += 1
print(x)

# 87
x = 0
for i in range(1, 5):
    for j in range(i):
        if j % 2 == 0:
            x += 1
        else:
            x -= 1
print(x)

# 88
x = 20
while x > 5:
    if x % 3 == 0:
        x -= 4
    else:
        x -= 3
print(x)

# 89
x = 0
for i in range(1, 8):
    if i == 5:
        continue
    if i % 3 == 0:
        x += i * 2
    else:
        x += i
print(x)

# 90
x = 0
for i in range(1, 6):
    for j in range(1, 5):
        if i + j > 5:
            break
        x += 1
print(x)

# 91
x = 1
for i in range(2, 6):
    if x % 2 == 0:
        x += i
    else:
        x *= i
print(x)

# 92
x = 0
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    x += i
    i += 2
print(x)

# 93
x = 0
for i in range(1, 5):
    for j in range(1, 5):
        if i == j:
            continue
        if (i + j) % 2 == 0:
            x += 1
        else:
            x -= 1
print(x)

# 94
x = 0
for i in range(1, 6):
    if i % 2 == 0:
        for j in range(i):
            if j == 2:
                break
            x += j
    else:
        x += i
print(x)

# 95
df = pd.DataFrame({"A":[10,20,30,40],"B":[5,15,25,35]})
df.loc[df["A"] > 20, "B"] += 10
print(df["B"].tolist())

# 96
df = pd.DataFrame({"Dept":["CS","AI","CS","AI","CS"],"Marks":[70,80,90,60,75]})
x = df.groupby("Dept")["Marks"].mean()
print(x["CS"])
print(x["AI"])

# 97
df = pd.DataFrame({"A":[1,2,3,4,5],"B":[10,20,30,40,50]})
x = df.loc[df["A"] % 2 == 1, "B"]
y = x * 2
print(x.tolist())
print(y.tolist())

# 98
df = pd.DataFrame({"Dept":["CS","AI","CS","AI"],"Marks":[60,90,80,70]})
df["Avg"] = df.groupby("Dept")["Marks"].transform("mean")
print(df["Avg"].tolist())

# 99
df = pd.DataFrame({"A":[3,1,4,2],"B":[30,10,40,20]})
x = df.sort_values("A")
x.loc[x["A"] > 2, "B"] *= 2
print(x["B"].tolist())
print(df["B"].tolist())

# 100
df = pd.DataFrame({"Dept":["CS","AI","CS","AI","CS"],"Marks":[70,85,60,75,90]})
x = df.groupby("Dept")["Marks"].transform(lambda s: s - s.mean())
y = df.loc[x > 0, "Marks"]
print(x.round(2).tolist())
print(y.tolist())