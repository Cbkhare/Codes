from math import factorial as F
from sys import stdin as si
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ind = [str(i) for i in range(1,n+1)]
        f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
        num =''
        new_n = n-1
        for i in range(n):
            #mi = F(new_n)
            mi = f[new_n]
            index = k//mi
            if k%mi==0:    # part of the rep
                index-=1
            num += ind.pop(index)
            k %=mi
            new_n-=1
        return num

    def getPermutation_1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ind = [str(i) for i in range(1,n+1)]
        num =''
        new_n = n-1
        for i in range(n):
            mi = F(new_n)
            index = k//mi
            if k%mi==0:    # part of the rep
                index-=1
            num += ind.pop(index)
            k %=mi
            new_n-=1
        return num

if __name__=="__main__":
    for i in range(int(si.readline().strip())):
        n,k = map(int,si.readline().strip().split())
        S = Solution()
        print(S.getPermutation(n,k))
