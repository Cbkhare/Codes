class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        from collections import OrderedDict as D
        d =  D()
        n = None
        m = None
        for i in range(len(A)):
            if A[i] not in d:
                t = B-A[i]
                if t not in d:
                    d[t]=i
            else:
                n = d[A[i]]
                m=i
                break
        #print (A,d,n,m)
        if not A or n is None or m is None:  return []
        return n+1, m+1