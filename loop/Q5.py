x=0
for i in range(1, 6):
    x += i
    if x % 3 == 0:
        continue
    print(x, end=" ")