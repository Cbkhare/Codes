from sys import stdin as si
from collections import Counter as c


class Solution:


    def bazinga(self,n,s):
        cr,cu = 0,0
        c = 0
        for i in range(n-1):
            if s[i]=='R':
                cr+=1
            else:
                cu+=1
            if cr==cu and s[i]==s[i+1]:
                c+=1
        return c

if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n = int(si.readline().strip())
    #m = list(map(int, si.readline().strip().split()))
    s = si.readline().strip()
    S = Solution()
    print(S.bazinga(n,s))


'''
http://codeforces.com/contest/935/problem/B
'''