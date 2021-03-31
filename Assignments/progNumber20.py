#There are a number of world cities contained in the file cities.csv download including city, country, and population.
#Write a program which will read the file and list how many cities are from each country.
#For example, the first few lines of your output should be:
    #Afghanistan:  1
    #Algeria:  1
    #Angola:  2
    #Argentina:  3
    #Armenia:  1
    #Australia:  5
    #Austria:  1

citiesFile = open("cities.csv", "r")
dictCities = {}

def printCountries(line, dictCities):
    print(line, ":", dictCities[line],"\n",end= "")

for i in citiesFile:
    i = i.split(",")
    if i[1] in dictCities.keys():
        dictCities[i[1]] += 1
    else:
        dictCities[i[1]] = 1

#The fun part to nicely touch up the assignment by alphabetically orderering the countries.
alphaCountries = list(dictCities.keys())
alphaCountries.sort()

for line in alphaCountries:
    printCountries(line, dictCities)