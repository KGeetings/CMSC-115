#Complete Exercise 26 on Page 267.  (For example, sending the string "abcdef" would return the string "fabcde".)

def rotate(string):
    return string[-1] + string[0:-1]

print(rotate(str(input("Enter a string: "))))