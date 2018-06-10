from sys import stdin as si
from collections import Counter as C


class Solution:

    def bazinga(self, k,t):
        self.k= k
        self.stack = []
        for i in range(len(t)):
            self.stack = [t[i]]
            self.toing(t[:i]+t[i+1:])

    def toing(self, d):
        x = self.stack[-1]
        if x*2 in d:
            i = d.index(x*2)
            self.stack.append(x*2)
            self.toing(d[:i] + d[i + 1:])
            self.stack.pop(-1)
        if x%3==0 and x//3 in d:
            i = d.index(x//3)
            self.stack.append(x//3)
            self.toing(d[:i] + d[i + 1:])
            self.stack.pop(-1)
        if d==[]:   print(*self.stack);exit


if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n = int(si.readline().strip())
    #m,n = map(int,si.readline().strip().split())
    #t = C(tuple(map(int,si.readline().strip().split())))
    l = list(map(int, si.readline().strip().split()))
    S = Solution()
    S.bazinga(n,l)