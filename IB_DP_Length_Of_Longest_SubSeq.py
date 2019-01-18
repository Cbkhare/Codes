class Solution:
    # @param A : tuple of integers
    # @return an integer

    def longestSubsequenceLength(self, A):
        if len(A) == 0: return 0
        self.dec = {}
        self.rdec = {}
        self.fun(A, 0)
        self.rfun(A, len(A) - 1)
        max_count = 0
        # print (A)
        # print (self.dec)
        # print (self.rdec)
        for i in range(len(A)):
            max_count = max(max_count, self.dec[i] + self.rdec[i] + 1)
        return max_count

    def fun(self, A, i):
        if i == len(A) - 1:
            self.dec[i] = 0
        else:
            self.fun(A, i + 1)
            count = 0
            for k, v in self.dec.items():
                if A[i] > A[k]:
                    count = max(count, v + 1)
            self.dec[i] = count
        return

    def rfun(self, A, i):
        if i == 0:
            self.rdec[i] = 0
        else:
            self.rfun(A, i - 1)
            count = 0
            for k, v in self.rdec.items():
                if A[i] > A[k]:
                    count = max(count, v + 1)
            self.rdec[i] = count
        return
