x = 1
for i in range(2, 6):
    for j in range(i, 0, -1):
        if x % 2 == 0:
            x += j
        else:
            x -= 1
    if x < 0:
        break
print(x, i, j)