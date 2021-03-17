import pylab

x = []
y = []
z = []

file = open("DJI.csv", "r")
lineNum = 0
days = 20

for line in file:
    if lineNum == 0:
        lineNum = 1
        continue
    columns = line.split(",")
    x.append(lineNum)
    y.append(float(columns[5]))
    if lineNum < days:
        z.append(float(columns[5]))
    else:
        runningAvg = sum(y[-days:])/days
        z.append(runningAvg)
    
    lineNum += 1
    
file.close()

pylab.plot(x, y, "b")
pylab.plot(x, z, "r")
pylab.show()