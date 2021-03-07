def cleanUp(x):
    x = x.lower()
    for punc in " ,.!@#$%^&*()-=_+{}[]|;:'":
        x = x.replace(punc, "")
    
    return x

def isPalindrome(s):
    s = cleanUp(s)
    
    if s == s[::-1]:
        return True
    else:
        return False

a = input("What is your word? ")
if isPalindrome(a):
    print("Yay! Your word is a palindrome.")
else:
    print("Nope. Not a palindrome.")