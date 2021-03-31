f = open("alice.txt","r")

wordCount = {}

alice = f.read()
aliceWords = alice.split()
f.close()

for word in aliceWords:
    word = word.lower()
    word = word.strip(".")
    word = word.strip("?")
    word = word.strip(",")
    word = word.strip("'")
    word = word.strip('"')
    
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

for i in range(10):
    maxWord = list(wordCount.keys())[0]
    
    for word in wordCount:
        if wordCount[word] > wordCount[maxWord]:
            maxWord = word
            
    print(f"The word '{maxWord}' appears {wordCount[maxWord]} times.")
    
    del(wordCount[maxWord])