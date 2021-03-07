#Complete Exercise 12 on Page 265 (include a program which asks the user for a year and uses your function to determine if it's a leap year.)

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


year = int(input("Enter a year: "))
isLeapYear(year)