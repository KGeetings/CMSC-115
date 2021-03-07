#Chapter 4, exercise 37:  Write a program that prompts for two words.  Print the longer word in all capitals and capitalize only the first letter of the second word.

wordOne = str(input("Enter your first word: "))
wordTwo = str(input("Enter your second word: "))

if len(wordOne) > len(wordTwo):
    print(wordOne.upper())
    print(wordTwo.capitalize())
else:
    print(wordTwo.upper())
    print(wordOne.capitalize())