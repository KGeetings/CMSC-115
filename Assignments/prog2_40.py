option = input("Enter 0 for metric, enter 1 for US customary: ")
optionInt = int(option)

if optionInt == 0:
    weightMet = input("Enter your weight in kilograms: ")
    heightMet = input("Enter your height in meters: ")
    
    weightMetInt = int(weightMet)
    heightMetInt = int(heightMet)
    
    bodyMassMet = weightMetInt / (heightMetInt ** 2)
    print("Your Body Mass Index (BMI) is:", bodyMassMet)
elif optionInt == 1:
    weightCust = input("Enter your weight in pounds: ")
    heightCust = input("Enter your height in inches: ")
    
    weightCustInt = int(weightCust)
    heightCustInt = int(heightCust)  
    
    weightConverted = weightCustInt / 2.205
    heightConverted = heightCustInt / 39.371
    
    bodyMassCust = weightConverted / (heightConverted ** 2)
    print("Your Body Mass Index (BMI) is:", bodyMassCust)
else:
    print("Please enter either 0 or 1.")