score_6 = "Score is 6"
score_5 = "Score is 5"
score_4 = "Score is 4"
score_3 = "Score is 3"
score_2 = "Score is 2"
score_1 = "Score is 1"
score_0 = "Score is 0"

secretWord = "elephant"
guessedLetters = ""

def getScore(word, letters):
    score = 0
    for letter in letters:
        if letter not in word:
            score += 1
    return score

def gameIsWon(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True
    
def gameOver(word, letters):
    if gameIsWon(word, letters):
        return True
    if getScore(word, letters) >= 6:
        return True
    
    return False


def printHangman(word, letters):
    score = getScore(word, letters)
    if score == 0:
        print(score_0)
    elif score == 1:
        print(score_1)
    elif score == 2:
        print(score_2)
    elif score == 3:
        print(score_3)
    elif score == 4:
        print(score_4)
    elif score == 5:
        print(score_5) 
    else:
        print(score_6)
    
    #Print the word, with correct letters filled in
    print()
    for letter in word:
        if letter in letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
    
    #Print the missed letters
    print()
    print("Missed letters:")
    for letter in letters:
        if letter not in word:
            print(letter, end="")
    print()


printHangman(secretWord, guessedLetters)
while not gameOver(secretWord, guessedLetters):
    newLetter = input("Guess a letter: ")
    if newLetter in secretWord:
        print("Yay, that's correct")
    else:
        print("You didn't get it right")
    guessedLetters += newLetter
    printHangman(secretWord, guessedLetters)
    
if gameIsWon(secretWord, guessedLetters):
    print("Nice")