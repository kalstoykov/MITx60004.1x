import string

def isPalindrome(aString):
    '''
    aString: a string
    Returns True if aString is a Palindrome
    String strips punctuation
    Returns False otherwise.
    '''
    alphabetStr = "abcdefghijklmnopqrstuvwxyz"
    newStr = ""
    # converting string to lower case and stripped of extra non alphabet characters
    aString = aString.lower()
    for letter in aString:
        if letter in alphabetStr:
            newStr += letter
    # if string is one letter or empty, it is a Palindrome
    if len(newStr) <= 1:
	return True
    # if string has more than 1 letter
    else:
        # reversing the string
        revStr = ''
        for i in range(len(newStr), 0, -1):
            revStr += newStr[i-1]
        # if string equals to reversed string, it is a Palindrome
        if list(newStr) == list(revStr):
            return True
    return False

# Test cases                        
print isPalindrome("Madam")  # returns True
print isPalindrome("Hello World") # returns False
print isPalindrome(" Madam")  # returns True    
print isPalindrome("1") # returns True 
