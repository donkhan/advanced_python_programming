x = 1
for i in range(2, 6):
    for j in range(i, 0, -1):
        if (i + j) % 2 == 0:
            x += j
        else:
            x -= i
    if x > 4:
        break

print(x, i, j)
