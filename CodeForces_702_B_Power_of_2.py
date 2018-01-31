from sys import stdin as si
from collections import Counter as c
from math import ceil as ce


class Solution:

    def __init__(self,mx):
        self.td = [1]
        x = 2
        while x < mx*2+1: #pow(10,9) * 4:
            self.td.append(x)
            x*=2

    def bazinga(self, m):
        ans = 0
        md = c(m)
        #print (md, m)
        for k in md:
            for x in self.td:
                if x > k and x-k in md and x-k!=k:
                    #print (k, x-k)
                    ans += md[k]*md[x-k]
                if x > k and x-k in md and x-k==k:
                    ans += (md[k]*(md[k]-1))
        print (ce(ans/2))


if __name__=='__main__':
    #for i in range(int(si.readline().strip())):
    n = si.readline().strip()
    m = list(map(int, si.readline().strip().split()))
    mx = max(m)
    S = Solution(mx)
    S.bazinga(m)


'''
123456789123456789
276193619183618162
'''