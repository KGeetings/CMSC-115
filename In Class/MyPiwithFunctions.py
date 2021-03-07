import random

def throwADart():
    x = random.random()
    y = random.random()
    if x*x + y*y < 1:
        return True
    else:
        return False

throws = 1000000
hits = 0

for i in range(throws):
    if throwADart():
        hits += 1
        
print("Pi is: ", (hits/throws)*4)