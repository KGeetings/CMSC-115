primes = []
lengthOfList = 100000

for i in range(lengthOfList):
    primes.append(True)
primes[0] = False
primes[1] = False

for current in range(2, lengthOfList):
    if primes[current]:
        for i in range(current * 2, lengthOfList, current):
            primes[i] = False

print(primes[23])