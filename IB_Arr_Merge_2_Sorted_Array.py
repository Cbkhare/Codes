class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        f= []
        i,j=0,0
        la,lb=len(A),len(B)
        if 0 in [la,lb]:    return A+B
        while i<la and j<lb:
            a,b = A[i],B[j]
            if a==b:
                f.extend([a,a])
                i+=1
                j+=1
            else:
                mi = min(a,b)
                f.append(mi)
                if a==mi:
                    i+=1
                else: #b==mi
                    j+=1
        return f + A[i:] + B[j:]

S = Solution()
A = [ 1, 4, 6, 8, 9, 9, 10 ]
B = [ 6, 9, 9, 15 ]

print (S.merge(A,B))