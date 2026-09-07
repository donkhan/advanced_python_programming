
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print("Enter the No")
n = int(input())
print(factorial(n))