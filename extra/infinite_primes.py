
def is_prime(n):
    for divisor in range(2, n-1):
        if n % divisor == 0:
            return False
    return True


def get_next_prime():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n = n + 1

g = get_next_prime()
for i in range(100):
    print(next(g))

