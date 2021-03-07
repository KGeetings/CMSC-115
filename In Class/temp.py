golfFile = open("temp.txt","r")
numLines = golfFile.readlines()

for i in range(0, len(numLines), 2):
    print("Name: " + numLines[i].strip("\n"))
    print("Score: " + numLines[i+1].strip("\n"))

print()