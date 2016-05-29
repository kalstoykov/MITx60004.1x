# MITx60004.1x

import string
import random

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)
    
def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])
    
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift     value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.

    dictionary = {'A':'A','B':'B','C':'C','D':'D','E':'E','F':'F','G':'G','H':'H','I':'I','J':'J','K':'K','L':'L','M':'M','N':'N','O':'O','P':'P','Q':'Q','R':'R','S':'S','T':'T','U':'U','V':'V','W':'W','X':'X','Y':'Y','Z':'Z','a':'a','b':'b','c':'c','d':'d','e':'e','f':'f','g':'g','h':'h','i':'i','j':'j','k':'k','l':'l','m':'m','n':'n','o':'o','p':'p','q':'q','r':'r','s':'s','t':'t','u':'u','v':'v','w':'w','x':'x','y':'y','z':'z'}    
    dict = {}
    
    for c in dictionary:
        if c in string.ascii_lowercase:
            index = string.ascii_lowercase.find(c)
            value = string.ascii_lowercase[((index + shift) % 26)]
            dict.update({str(c):str(value)})
        elif c in string.ascii_uppercase:
            index = string.ascii_uppercase.find(c)
            value = string.ascii_uppercase[((index + shift) % 26)]
            dict.update({str(c):str(value)})
    return dict
            
            
    
    

    
    
    
            
                
