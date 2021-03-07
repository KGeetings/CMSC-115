userInput= float(input("Enter a number, 0 will stop the program: "))
total = 0

while userInput !=0:
    total += userInput
    userInput= float(input("Enter a number, 0 will stop the program: "))
    
print("The total is", total)