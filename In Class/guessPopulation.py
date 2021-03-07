userYear = int(input("What year do you want to see the predicted population? "))
additionalYears = 2021 - userYear

popChangePerSecond = 1/7 + 1/13 + 1/35
popChangePerYear = popChangePerSecond * 365 * 24 * 60 * 60
currentPop = 307357840
predictPop = currentPop + (popChangePerYear * additionalYears)

print("The predicted population in the year," userYear, "will be", predictPop)
