def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1
    return testValue        

#Test cases
print gcdIter(2, 12)        # 2
print gcdIter(6, 12)        # 6     
print gcdIter(9, 12)        # 3
print gcdIter(17, 12)       # 1
