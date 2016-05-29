#  a program that prints the longest substring of s in which the letters occur in alphabetical order.
#  For example, if s = 'azcbobobegghakl', the outut is: Longest substring in alphabetical order is: beggh

longest = ''
case = s[0]      
   
for num in range(1, len(s)):   
    if len(case) > len(longest):
       longest = case
    if s[num] > s[num-1]:
       case = case + s[num]  
    elif s[num] == s[num-1]:
       case = case + s[num-1]   
    else:                     
       case = s[num]

print "Longest substring in alphabetical order is: ", longest

# Test cases:
s = 'iprhiwostabaayzd'              # Longest substring in alphabetical order is:  aayz
s = 'kwhbwovajhelte'                # Longest substring in alphabetical order is:  elt
s = 'wlkvauhlsakwztpwyu'            # Longest substring in alphabetical order is:  akwz
s = 'lpjiwmitwwir'                  # Longest substring in alphabetical order is:  itww
s = 'fmcfavtcyej'                   # Longest substring in alphabetical order is:  fm
s = 'zyxwvutsrqponmlkjihgfedcba'    # Longest substring in alphabetical order is:  z
