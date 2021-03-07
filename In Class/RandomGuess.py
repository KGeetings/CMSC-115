import random

low = 1
high = 100
secret= random.randrange(low,high + 1)
hasGuessedIt = False
numGuesses = 0
print("I have a number from 1 to 100...")

while not hasGuessedIt:
    guess = int(input("Decide: "))
    numGuesses += 1
    if guess == secret:
        print("Congrats, you got it.")
        hasGuessedIt = True
    elif guess > secret:
        print("Your guess was too high.")
    else:
        print("Your guess was too low.")

print("That took you", numGuesses, "to get right.")