from math import sqrt

class Solution:
    def allFactors(self, A):
        l = []
        r = []
        for i in range(1,int(sqrt(A))+1):
            if A%i == 0:
                l.append(i)
            if A//i != 1 and A//i != i:
                r = [int(A/i)] + r
        return l + r
    