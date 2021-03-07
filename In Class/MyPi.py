import math
import random

#Program that calculates Pi, based off of a mathematical formula

#my_pi = 0

#for i in range (1,10000000,2):
    #if (i-1) % 4 == 0:
        #my_pi = my_pi + 4/i
    #else:
        #my_pi = my_pi - 4/i

    #if (i-1) % 1000000 == 0:
        #print("After", i, "terms, my pi is", my_pi, ". And that is off by", math.fabs(math.pi-my_pi))


#Program that calculates Pi, by guessing (throwing 1,000,000 darts at a circle)

num_hits = 0
num_darts_to_throw = 100000000

for i in range(1,num_darts_to_throw):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1

    if x*x + y*y <= 1:
        num_hits += 1
    if i % 1000000 == 0:
        my_pi = num_hits / i * 4
        print("I calculated Pi as", my_pi)    

my_pi = num_hits / num_darts_to_throw * 4
print("I calculated Pi as", my_pi)
