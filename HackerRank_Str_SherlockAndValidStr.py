import sys
from collections import Counter as c
from functools import reduce as r
from operator import itemgetter as ig


def isValidCase1(d):
    if len(d) == 1:
        return True
    else:
        return False


def isValidCase2(d):
    if len(d) != 2:
        return False
    else:
        len_one = list(filter(lambda x: len(d[x]) == 1,
                              d))  # The ones whose count is not equal to others
        len_not_one = list(filter(lambda x: len(d[x]) != 1, d))
        # The number of unequal element should be one
        # If it is one the diffenece of the count should also be one
        #print (len_one, len_not_one)
        if len(len_one) == 1 and \
                (len_one == [1] or abs(len_one[0] - len_not_one[0]) == 1):
            return True
    return False


def isValid(s):
    s = ''.join(sorted(s))
    d = {}
    i, l = 0, len(s)
    while i < l:
        c, j, found = 1, i, False
        while i + 1 < l and s[i] == s[i + 1]:
            c += 1
            i += 1
            found = True
        d[c] = [s[j]] + d.get(c, [])
        i += 1
    print(d)
    if bool(isValidCase1(d) or isValidCase2(d)):
        return 'YES'
    else:
        return 'NO'

if __name__=='__main__':
    for i in range(int(input())):
        s = input().strip()
        result = isValid(s)
        print(result)

'''
https://www.hackerrank.com/challenges/sherlock-and-valid-string
'''