class Solution:
    # @param A : string
    # @return an integer
    def __init__(self):
        self.s = ('A','E','I','O','U',
                    'a','e','i','o','u')
        self.ns = ()
    def solve(self, A):
        count = 0
        l = len(A)
        for i in range(l):
            if A[i] in self.s:
                sl = l-i
                count += sl
        return count%10003