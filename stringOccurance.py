# A program that prints the number of times the string 'pop' occurs in s
# if s = 'azcpopopegghakl', the output is: Number of times pop occurs is: 2

x = 0
countStr = 0
for x in range(0, len(s) - 2):
    if s[x:x+3] == 'pop':
        countStr += 1
print('Number of times pop occurs is: ' + str(countStr))

# Test Cases
s = 'iiqkeizyok'                       # Number of times pop occurs is: 0
s = 'popopopopopopopopopopopopopop'    # Number of times pop occurs is: 14
s = 'bppopppxpopptpo'                  # Number of times pop occurs is: 2

