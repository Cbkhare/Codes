from sys import stdin as si
from collections import Counter as c


class Solution:

    def checkSquare(self, x):
        return x**.5%1 == 0

    def bazinga(self,b):
        b.sort()
        for i in b[::-1]:
            if i<0: return i
            if not self.checkSquare(i):
                return i


if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n = si.readline().strip()
    m = list(map(int, si.readline().strip().split()))
    S = Solution()
    print(S.bazinga( m))


'''
http://codeforces.com/contest/914/problem/A
'''
