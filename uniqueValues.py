def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    ans = []
    for k, v in aDict.items():
        if aDict.values().count(v) == 1:
            ans.append(k)
        else:
            ans
    return sorted(ans)
