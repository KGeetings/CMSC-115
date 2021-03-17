#Write a function that takes a list of integers as an argument and returns a list of three of the integers whose sum is zero. Return an empty list if no such integer exist.

inputList= input('Enter elements of a list separated by spaces: ')
lst = inputList.split()

for i in range(len(lst)):
    lst[i] = int(lst[i])
    
emptyList = []

def sumInt(lst, n):
    foundThree = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (lst[i] + lst[j] + lst[k] == 0):
                    emptyList.append(lst[i])
                    emptyList.append(lst[j])
                    emptyList.append(lst[k])
                    print(emptyList)
                    del emptyList[:]
                    foundThree = True
    if (foundThree == False):
        print(emptyList)

sumInt(lst, len(lst))