def averageNumber(a,b,c):
    import statistics
    theAverage = statistics.fmean([a,b,c])
    return theAverage

a = 3
b = 5
c = 7

print("The average of {}, {}, and {} is: {}.".format(a,b,c, averageNumber(a,b,c)))
