#Chapter 4, exercise 44:  Write a program that prompts for a sentence, and calculates the number of uppercase letters, 
#lowercase letters, digits, and punctuation.  Output the results neatly formatted and labeled in columns.
import string

userSent = str(input("Enter a sentence: "))
uppercase = 0
lowercase = 0
digits = 0
punctuation = 0

for letters in range(len(userSent)):
    if userSent[letters].isupper():
        uppercase += 1
    elif userSent[letters].islower():
        lowercase += 1
    elif userSent[letters].isdigit():
        digits += 1

for i in userSent:
    if i in string.punctuation:
        punctuation += 1

print("{:15}{:15}{:15}{:15}".format("uppercase","lowercase","digits","punctuation"))
print("{:15}{:15}{:15}{:15}".format("---------","---------","------","-----------"))
print("{}{:15}{:15}{:15}".format(uppercase,lowercase,digits,punctuation))