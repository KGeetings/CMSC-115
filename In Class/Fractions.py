import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numer = numerator
        self.denom = denominator
    def __add__(self, other):
        #n = self.numer * other.denom + other.numer * self.denom
        #d = self.denom * other.denom
        #answer = Fraction(n,d)
        #return answer
        return Fraction(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)
    def __gt__(self, other):
        a = self.numer / self.denom
        b = other.numer / other.denom
        return (a > b)
    def __sub__(self, other):
        return Fraction(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)
    def __mul__(self, other):
        return Fraction(self.numer * other.numer, self.denom * other.denom)
    def __str__(self):
        n = self.numer
        d = self.denom
        x = math.gcd(n,d)
        n = n // x
        d = d // x
        if n >= d:
            whole = n // d
            n = n % d
            return str(whole) + " " + str(n) + "/" + str(d)
        else:
            return str(n) + "/" + str(d)

#Tester code

#a = Fraction(3,4)
#b = Fraction(7,12)

#if a > b:
#    print("A is bigger")
#else:
#    print("B is bigger")

#c = a + b
#d = a - b
#e = a * b

#print(f"{a} + {b} = {c}")
#print(f"{a} - {b} = {d}")
#print(f"{a} * {b} = {e}")