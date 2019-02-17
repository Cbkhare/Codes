class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct1(self, A):
        if not A:
            return -1
        res = cur =  A[0]
        minp=None
        for i in range(1, len(A)):
            t = cur*A[i]
            if A[i]==0:
                cur = 1 #reset 
                minp = None #rest
                res = max(res,A[i])   #to phase out neg values
            elif t<cur:
                if not minp:
                    minp = t
                    cur = 1 #reset 
                else:
                    cur = cur*A[i]*minp # now cur is positive 
                    res = max(cur,A[i],res)
                    minp= None#reset
            else:
                cur = cur*A[i]
                res = max(cur,res)
        return res 
    
    def maxProduct(self, A):
        return max(self.maxProduct1(A), self.maxProduct1(A[::-1]))
