price = float(input("Enter the price of your meal: "))
age = int(input("Enter your age: "))

if age >= 55:
    print("Your total is", round((price * 1.07 * .85),2))
else:
    print("Your total is", round((price * 1.07),2))