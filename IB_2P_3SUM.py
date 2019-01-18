class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        i = 0
        j = i + 1
        k = len(A) - 1
        from sys import maxsize as m
        mn = m
        ns = sum(A)
        # print(A)
        for i in range(len(A)):
            j = i + 1
            k = len(A) - 1
            while j < k:
                t = A[j] + A[k]
                tar = abs(A[i] + t - B)
                # print (A[i],A[j],A[k],B,tar,mn)
                if tar < mn:
                    mn = tar
                    ns = A[i] + t
                if B == A[i] + t:
                    return A[i] + t
                if A[i] + t > B:
                    k -= 1
                elif A[i] + t < B:
                    j += 1
            j = i + 1
            k = j + 1
            i += 1
            # print(i,j,k)
        return ns
