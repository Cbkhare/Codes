class Solution:
    # @param A : integer
    # @return a list of integers

    def sieve(self, A):

        x = [1 for i in range(A + 1)]
        p = []
        for i in range(2, A + 1):
            if x[i] == 1:
                p.append(i)
                for j in range(i, A + 1, i):
                    x[j] = 0
        return p
