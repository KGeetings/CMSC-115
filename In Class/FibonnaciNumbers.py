fib = [1,1]

#for i in range(98):
    #fib.append(fib[-1] + fib[-2])
    #if (fib[i]) >= 1000:
        #print(fib[i])
        #break
    
fib_num = 2
while len(str(fib[-1])) < 1000:
    fib.append(fib[-1] + fib[-2])
    fib_num += 1

print(fib_num)