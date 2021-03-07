def getRidOfVowels(s):
    for vowels in "aeiou":
        s = s.replace(vowel, "")
        s = s.replace(vowel.upper, "")
    
    return s

inFile = open("alice.txt","r")
outFile = open("alice-no-vowels.txt","w")

for line in inFile:
    line = line.upper()
    outFile.write(line)

inFile.close()
outFile.close()