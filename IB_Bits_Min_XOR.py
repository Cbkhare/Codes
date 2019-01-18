class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A.sort()
        x = 100000
        for i in range(len(A)-1):
            x = min(x,A[i]^A[i+1])
        return x