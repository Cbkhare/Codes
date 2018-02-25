from collections import Counter as c
from sys import stdin as si


class Solution:
    def bazinga(self, n, t):
        g = [0]*n
        s = sum(t)
        if bool(s%3):   return 0
        s//=3
        a=c= 0
        for i in range(n-1,-1,-1):
            a+=t[i]
            if a==s:
                c+=1
            g[i]=c
        print (g)
        a=c= 0
        for j in range(n-2):
            a+=t[j]
            if a==s:
                c+=g[j+2]
        return c

if __name__ == '__main__':
    for i in range(int(si.readline().strip())):
        n = int(si.readline().strip())
        x = list(map(int, si.readline().strip().split()))
        S = Solution()
        print (S.bazinga(n,x))
