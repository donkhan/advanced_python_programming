x = 0
for i in range(1, 6):
    for j in range(1, i + 1):
        if j == 3:
            continue
        x += i - j
    if x >= 5:
        break
print(x, i, j)