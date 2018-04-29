from sys import stdin as si
from collections import Counter as c


class Solution:


    def bazinga(self,n,m,s):
        for i in range(m):
            s = s.replace('BG','GB')
        return s


if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n,m = map(int, si.readline().strip().split())
    #m = list(map(int, si.readline().strip().split()))
    s = si.readline().strip()
    S = Solution()
    print(S.bazinga(n,m,s))


'''
http://codeforces.com/contest/266/problem/C
'''