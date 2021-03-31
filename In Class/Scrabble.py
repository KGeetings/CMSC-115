import random

def getRandomLetters():
    bag = []
    for letter in "kjxqz":
        bag.append(letter)
    for letter in "bcmpfhvwy":
        for i in range(2):
            bag.append(letter)
    for letter in "g":
        for i in range(3):
            bag.append(letter)
    for letter in "lsud":
        for i in range(4):
            bag.append(letter)
    for letter in "nrt":
        for i in range(6):
            bag.append(letter)
    for letter in "o":
        for i in range(8):
            bag.append(letter)
    for letter in "ai":
        for i in range(9):
            bag.append(letter)
    for letter in "b":
        for i in range(12):
            bag.append(letter)
    
    letters = ""
    for i in range(7):
        myLetter = random.randrange(len(bag))
        letters += (bag[myLetter])
        del(bag[myLetter])
    
    return letters

def canISpellWith(word, letters):
    for char in word:
        if word.count(char) > letters.count(char):
            return False
    
    return True

def getScrabbleScore(word, pointValues):
    score = 0
    for letter in word:
        score += pointValues[letter]
    return score
    
letterPoints = {}

for letter in "eaionrtlsu":
    letterPoints[letter] = 1
for letter in "dg":
    letterPoints[letter] = 2
for letter in "bcmp":
    letterPoints[letter] = 3
for letter in "fhvwy":
    letterPoints[letter] = 2
letterPoints["k"] = 5
for letter in "jx":
    letterPoints[letter] = 8
for letter in "pq":
    letterPoints[letter] = 10

myLetters = getRandomLetters
print(f"My letters are {myLetters}")

f = open("words.txt", "r")
words = f.read().split()
f.close()

realWords = []

for word in words:
    if word[0].islower():
        realWords.append(word)

bestWord = ""

for word in words:
    if canISpellWith(word,myLetters):
        if getScrabbleScore(bestWord,letterPoints) < getScrabbleScore(word,letterPoints):
            bestWord = word
            
        #print(f"{word} is worth {getScrabbleScore(word,letterPoints)} points?")

print(f"The best word was {bestWord}, with a score of {getScrabbleScore(bestWord,letterPoints)}")