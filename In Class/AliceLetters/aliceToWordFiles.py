for letter in "qwertyuiopasdfghjklzxcvbnm":
    #Open the input file (alice)
    inFile = open("alice.txt","r")
    #Open the output file (letter.txt)
    outFile = open(letter + ".txt", "w")
    #Read through line by line
    for line in inFile:
        
        #Read through word-by-word
        for word in line.split():
            word = word.strip()
            for punctuation in "\"',.!?:;":
                word = word.strip(punctuation)
            word = word.lower()
            
            #If word starts with letter
            if word[0] == letter:
                #output the word to the output file
                outFile.write(word + "\n")
                
    #Close the files
    inFile.close()
    outFile.close()