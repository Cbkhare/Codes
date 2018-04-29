from sys import stdin as si
#from collections import Counter as c
from sys import maxsize as mx


class Solution:

    def bazinga(self, n, m, l):
        l.sort()
        d = mx
        for i in range(0,m-n+1):
            d = min(d,l[i+n-1]-l[i])
        return(d)


if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    #n = int(si.readline().strip())
    n,m = map(int, si.readline().strip().split())
    l = list(map(int, si.readline().strip().split()))
    S = Solution()
    print(S.bazinga(n,m,l))


'''
http://codeforces.com/contest/337/problem/A
'''