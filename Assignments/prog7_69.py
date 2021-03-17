#Using pylab draw a graph of equation y = sin(x)/x from -6pi to 6pi.

import pylab
import math

pi = math.pi
i = -6 * pi
t = 1200
step = pi / 100
x = []
y = []

def f(xValue):
    return math.sin(xValue)/xValue

for t in range(t + 1):
    if i >= (-6*pi) and i <= (6*pi):
        x.append(i)
        y.append(f(i))
        i += step
    t += 1

pylab.plot(x,y, "b")
pylab.show()