listOfNumbers = []
number = 100

while number <= 1000:
    number += 1
    if number % 17 == 0:
        listOfNumbers.append(number)
        
print(listOfNumbers)