import statistics

number1 = float(input("What is your first number? "))
number2 = float(input("What is your second number? "))
number3 = float(input("What is your third number? "))

avg = statistics.fmean([number1,number2,number3])

print("The average of these numbers is", avg)