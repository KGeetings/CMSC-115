def wordIsTypable(word, listOfLetters):
    for letter in word:
        if letter not in listOfLetters:
            return False
    return True

left_hand = "qwertasdfgzxcvb"

my_file = open("words.txt", "r")
num_words = 0
longest_word = ""

for line in my_file:
    line = line.strip()
    line = line.lower()
    if wordIsTypable(line, left_hand):
        if len(line) >= len(longest_word):
            print(line)
            longest_word = line
    
my_file.close()
print(longest_word)