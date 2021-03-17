import math
import pylab

def f(x):
    return math.sin(x**2) * x + x**3

def integrate(func, a, b, num):
    h = (b-a)/num
    total = 0
    
    for i in range(num):
        x = a + (i+.5)*h
        y = func(x)
        area = y * h
        total += area
    return total

y = []
x = []

for i in range(120):
    x.append(i/10)
    y.append(f(x[-1]))
    
#pylab.plot(x,y,"b")
#pylab.show()

print("The area under the curve of f(x) from 3 to 9 is:", integrate(f, 3, 9, 100000))