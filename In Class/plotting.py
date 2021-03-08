import matplotlib
import pylab
import math

x = []
y = []

for i in range(100):
    x.append(i/20)
    y.append(math.sin(i/20))

pylab.plot(x, y, "r+")

pylab.show()