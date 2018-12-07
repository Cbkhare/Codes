class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        if A=="":   return 0
        A = A.strip()
        st = ""
        for i in range(len(A)-1,-1,-1):
            if A[i]==" ": break
            st+=A[i]
        return len(st)