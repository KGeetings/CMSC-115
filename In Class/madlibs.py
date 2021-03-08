import random

def getListFromFile(filename):
    x = []
    theFile = open(filename, "r")
    for line in theFile:
        x.append(line.strip())
    
    theFile.close()
    return x

adjectives = getListFromFile("adjectives.txt")
nouns = getListFromFile("nouns.txt")
verbs = getListFromFile("verbs.txt")

print(f"{random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)}ed the {random.choice(adjectives)} {random.choice(nouns)}.")
