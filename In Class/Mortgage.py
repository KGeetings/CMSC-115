principle = float(input("How big is the mortgage? "))
interestRate = float(input("What is the interest rate in percent? "))/100
monthlyPayment = float(input("How large is the monthly payment? "))

month = 1
print("Date     Principle     Interest      Payment     New Principle")
print("----     --------      -------       -------     -------------")

while principle > 0:
    monthlyInterest = principle * (interestRate / 12)
    newPrinciple = principle - monthlyPayment + monthlyInterest
    print(month, 
          round(principle,2), 
          round(monthlyInterest,2), 
          monthlyPayment, 
          round(newPrinciple,2))
    principle = newPrinciple
    month += 1