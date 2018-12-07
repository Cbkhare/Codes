from sys import stdin as si
from math import log, ceil, floor

class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        count=0
        for i in range(2,int(log(A,2))+1):
            count+=1
            t = int(A**(1/i))
            if t==1: break
            if t**i==A or (t+1)**i == A:
                print(count)
                return 1
        print(count)
        return 0

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        n = int(si.readline().strip())
        print (S.isPower(n))
