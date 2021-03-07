n = int(input("Enter a number: "))

i = 2
while i <= n // 2:
    if n % i == 0:
        print("The number is not prime")
        isPrime = False
        i += 1
if isPrime == True:
    print(n, "is prime")

        