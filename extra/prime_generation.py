def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    n = n + 1
    while is_prime(n) == False:
        n = n + 1
    return n

print(next_prime(13))
print(next_prime(17))

