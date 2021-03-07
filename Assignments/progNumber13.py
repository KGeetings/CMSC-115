#Write a program which will read the dictionary file (words.txt), 
#and calculate the answer to the question: "What percentage of words have more vowels than consonants?"

file = open("words.txt","r") 

vowelWords = 0
counter = 0

content = file.read() 
newList = content.split("\n") 

for line in file:
    line = line.upper()

#attempt at making a very verbose for loop that is not optimized at all
for i in newList:
    if i:
        counter += 1
    vowelsInWord = 0
    consonantsInWord = 0
    for l in range(len(i)):
        if i[l] == "A" or i[l] == "E" or i[l] == "I" or i[l] == "O" or i[l] == "U" or i[l] == "a" or i[l] == "e" or i[l] == "i" or i[l] == "o" or i[l] == "u":
            vowelsInWord += 1
        if i[l] == "Q" or i[l] == "W" or i[l] == "R" or i[l] == "T" or i[l] == "Y" or i[l] == "P" or i[l] == "S" or i[l] == "D" or i[l] == "F" or i[l] == "G" or i[l] == "H" or i[l] == "J" or i[l] == "K" or i[l] == "L" or i[l] == "Z" or i[l] == "X" or i[l] == "C" or i[l] == "V" or i[l] == "B" or i[l] == "N" or i[l] == "M" or i[l] == "q" or i[l] == "w" or i[l] == "r" or i[l] == "t" or i[l] == "y" or i[l] == "p" or i[l] == "s" or i[l] == "d" or i[l] == "f" or i[l] == "g" or i[l] == "h" or i[l] == "j" or i[l] == "k" or i[l] == "l" or i[l] == "z" or i[l] == "x" or i[l] == "c" or i[l] == "v" or i[l] == "b" or i[l] == "n" or i[l] == "m":
            consonantsInWord += 1
    if vowelsInWord > consonantsInWord:
        vowelWords += 1

percentage = (vowelWords/counter)*100

file.close()
print(f"The percentage of words that have more vowels than consonants is {percentage:.2f}%")