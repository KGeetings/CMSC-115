#golfFile = open("temp.txt","r")
#numLines = golfFile.readlines()

#for i in range(0, len(numLines), 2):
    #print("Name: " + numLines[i].strip("\n"))
    #print("Score: " + numLines[i+1].strip("\n"))

#print()

#change = int(input("Enter change: "))
#while change >= 100 or change < 0:
    #change = int(input("Amount of change must be between 0 and 99."))

#print("Quarters:", change//25)
#change = change%25
#print("Dimes:", change//10)
#change = change%10
#print("Nickels:", change//5)
#change = change%5
#print("Pennies:", change//1)

firstStock = 1
secondStock = 1
thirdStock = 1
fourthStock = 1

firstStock = float(input("Enter amount invested in SPY: "))
if firstStock < 0:
    print("Value must be positive.")
    quit()

secondStock = float(input("Enter amount invested in QQQ: "))
if secondStock < 0:
    print("Value must be positive.")
    quit()

thirdStock = float(input("Enter amount invested in EEM: "))
if thirdStock < 0:
    print("Value must be positive.")
    quit()
    
fourthStock= float(input("Enter amount invested in VXX: ")) 
while fourthStock < 0:
    print("Value must be positive.")
    quit()

total = firstStock + secondStock + thirdStock + fourthStock
firstStockPer = (firstStock/total)*100
secondStockPer = (secondStock/total)*100
thirdStockPer = (thirdStock/total)*100
fourthStockPer = (fourthStock/total)*100

print("ETF PERCENTAGE")
print("--------------------")
print(f"SPY {firstStockPer:.2f}%")
print(f"QQQ {secondStockPer:.2f}%")
print(f"EEM {thirdStockPer:.2f}%")
print(f"VXX {fourthStockPer:.2f}%")
print(f"TOTAL AMOUNT INVESTED: ${total:,.2f}")

