from sys import stdin as si
from operator import itemgetter as g

class Solution:

    def maximumGap(self, A):
        if A == []: return -1
        A = sorted(list(enumerate(A)), key=g(1))
        mn, mx=len(A)-1,0
        diff=-1
        for i,j in A:
            if i<mn:
                mn=i
            diff = max(diff, i-mn )
        return diff

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        print (S.maximumGap(list(map(int,si.readline().strip().split()))))
