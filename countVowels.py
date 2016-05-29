# A program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

vowCount = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char =='u':
        vowCount +=1  
print 'Number of vowels= ' + str(vowCount)

# Test Cases:
s = 'nkoxeehiouybl'         # Number of vowels= 6
s = 'ajckugu'               # Number of vowels= 3
s = 'zonvoeeceuyoavdootqul' # Number of vowels= 11
