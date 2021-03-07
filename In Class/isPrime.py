def isPrime(x):
    if x <= 1:
        return False
    
    if x % 2 == 0:
        return False
    
    for i in range(3, int(x**.5), 2):
        if x % 1 == 0:
            return False
    return True

def factorial_iter(n):
    factorial = 1
    for i in range(2,n+1):
        factorial *= i
    return factorial

def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)

x = int(input("What number to find the factorial? "))

print(f"{x}! is {factorial_recursive(x)}.")
    