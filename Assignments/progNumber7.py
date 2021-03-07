tripSum = 1000

for a in range(tripSum):
    for b in range(tripSum):
        c = tripSum - (a + b)
        if (a**2) + (b**2) == (c**2) and (a < b) and (b < c):
            print("Your values are: a =", a, " b =", b, " and c =",c)