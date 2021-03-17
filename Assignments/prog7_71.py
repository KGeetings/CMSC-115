#Write a program that prompts for two sentences and prints the combined words in alphabetical order. Ignore case and discard punctuation.

sentence1 = str(input("Enter the first sentence: "))
sentence2 = str(input("Enter the second sentence: "))
combSent = sentence1 + " " + sentence2

def mutilate(s):
    for punc in ",.:\"'[]{}!?+_-;()@#$%^&/*=`~":
        s = s.replace(punc, "")
    return s

combSentStrip = mutilate(combSent)
words = [word.lower() for word in combSentStrip.split()]
words.sort()

alphabetLst = []
print("The combined words in alphabetical order are: ")
for word in words:
    alphabetLst.append(word)
    
print(alphabetLst)
