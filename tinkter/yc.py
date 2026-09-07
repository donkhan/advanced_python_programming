import numpy as np

yl = np.array([1,2,-2])

c = 0
for e in yl:
    if e < 0:
        c = c + 1

print(c)

print(len(yl[yl < 0]))

#help(yl)


print(list(zip([1,2,3],[4,5])))

