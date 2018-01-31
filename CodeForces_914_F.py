from sys import stdin as si
from collections import Counter as c
import re

class Solution:

    def bazinga21(self, string, sub):
        count = start = 0
        while True:
            start = string.find(sub, start) + 1
            if start > 0:
                count += 1
            else:
                return count

    def bazinga2(self, S, P):
        i, j = 0, len(P) - 1
        c = 0
        while j < len(S):
            if S[i:j + 1] == P:
                c+=1
            i += 1
            j += 1
        return c

    def bazinga1(self, a, i,c):
        return a[:i]+c+a[i+1:]


if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n = list(si.readline().strip())
    m = int(si.readline().strip())
    S = Solution()
    for i in range(m):
        m = si.readline().strip().split()
        if m[0]=='1':
            #n = S.bazinga1(n,int(m[1])-1,m[2])
            n[int(m[1])-1] = m[2]
        else:
            x = S.bazinga2(''.join(n[int(m[1])-1:int(m[2])]), m[3])
            print (x)

'''
http://codeforces.com/contest/914/problem/F
'''