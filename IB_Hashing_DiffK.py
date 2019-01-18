class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible_old(self, A, B):
        if not A: return 0
        x1 = set()
        x2 = set()
        AA = [-1 * A[i] for i in range(len(A))]
        # A = [A[i] + B for i in range(len(A))]
        for i in range(len(A)):
            v1 = B + A[i]
            v2 = B + AA[i]

            if A[i] in x1 or AA[i] in x2:  # or A[i] in x2:
                return 1
            else:
                x1.add(v1)
                x2.add(v2)
        return 0

    def diffPossible(self, A, B):
        if not A: return 0
        x1 = set()
        for i in range(len(A)):
            if A[i] in x1:
                return 1
            else:
                v1 = B + A[i]
                v2 = A[i] - B
                x1.update({v1, v2})
        return 0

