theFile = open("alice.txt", "r")

def mutilate(s):
    for punc in ",.:\"'[]{}!?+_-;()@#$%^&/*=`~":
        s = s.replace(punc, "")
    return s
    

wholeThing = theFile.read()
theFile.close()
words = wholeThing.split()
wordCount = len(words)

totalWordLetters = sum([len(mutilate(i)) for i in words])


avgWordLength = totalWordLetters / wordCount
print("The average word length is: ", avgWordLength)