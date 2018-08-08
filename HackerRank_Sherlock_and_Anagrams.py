from sys import stdin as si
from math import factorial as f

global d

def nCr(n,r):
    return f(n) / f(r) / f(n-r)

def bazinga(S, l, i):
    if i==l-1:
        d[S[i]] = 1
        return [S[i]]
    else:
        lst = bazinga(S, l, i+1)
        c = S[i]
        new_lst = [c]
        d[c] = 1 if c not in d else d[c] + 1
        for j in range(l-i-1):
            new_str = c+lst[j]
            new_lst.append(c+lst[j])
            new_str_sort = ''.join(sorted(new_str))
            d[new_str_sort] = 1 if new_str_sort not in d else d[new_str_sort] +1
        return new_lst

def sherlockAndAnagrams(s):
    _ = bazinga(s,len(s),0)
    count = 0
    for k,v in d.items():
        if v==1:    continue
        else:
            count += nCr(v,2)
    return int(count)


if __name__=="__main__":
    for i in range(int(si.readline().strip())):
        d = {}
        print (sherlockAndAnagrams(si.readline().strip()))

'''
https://www.hackerrank.com/challenges/sherlock-and-anagrams

Hint:-
1) Find all the substring in the string and insert it into a Hash d
2) Check for each substring s, if sorted(s) exist in Hash d '''