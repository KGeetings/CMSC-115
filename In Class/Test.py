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

print("Uppercase:\t",uppercase,"\nlowercase:\t",lowercase)