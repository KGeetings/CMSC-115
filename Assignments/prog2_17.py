import math

isPerfectSquare = False

while isPerfectSquare == False:
    userNumber = math.sqrt(int(input("Input a number: ")))
    if userNumber % 1 == 0:
        isPerfectSquare = True
else:
    print("You found a perfect square!")