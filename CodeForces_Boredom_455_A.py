from sys import stdin as si
from collections import Counter as C

class Solution(object):

    def __init__(self):
        self.result = {}

    def toing(self, A):
        self.D = C(A)
        return self.bazinga(max(self.D))

    def bazinga(self,n):
        if n in self.result:
            return self.result[n]
        if n not in self.D:
            n-=1
        if n <=0:   return 0
        else:
            out = max(self.bazinga(n-1), self.bazinga(n-2)+(n*self.D[n]))
            self.result[n] = out
        return self.result[n]

    def toing1(self, A):
        d = [0]*100001
        for x in A:
            d[x] += x
        a = b = 0
        for i in d:
            a, b = max(a, i + b), a
        return (a)

if __name__=="__main__":
    x = si.readline().strip()
    y = map(int, si.readline().strip().split())
    S = Solution()
    print (S.toing(y))

'''
In this task we need to maximize the sum of numbers that we took. Let precalc array cnt. cnt[x] ? number of integers x in array a. Now we can easily calculate the DP:

f(i)=max(f(i-1),f(i-2)+cnt[i]*i), 2?i?n;

f(1)=cnt[1];

f(0)=0;

The answer is f(n).

Asymptotics - O(n).
'''