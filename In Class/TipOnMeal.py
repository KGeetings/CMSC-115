costOfMeal = float(input("How much did your meal cost? (before tax) "))
amountOfTip = float(input("What percentage do you want to tip? "))

the_tip = costOfMeal * amountOfTip / 100
the_tip = int(the_tip * 100) / 100

print("Add $", the_tip, " to your meal.",sep="")