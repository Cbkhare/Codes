from sys import maxsize as M


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        def fx(a, b, c):
            return abs(max(a, b, c) - min(a, b, c))
        mn = M
        i=j=k=0
        la,lb,lc=len(A),len(B),len(C)
        if 0 in [la, lb, lc]: return M
        count = la+lb+lc
        while i<la or j<lb or k<lc:
            #print (i,j,k)
            a,b,c = A[i],B[j],C[k]
            mn = min(fx(a,b,c), mn)
            mi = min(a,b,c)
            if a==mi and i<la-1:
                i+=1
            if b==mi and j<lb-1:
                j+=1
            if c==mi and k<lc-1:
                k+=1
            count -=1
            if count==0:    break
        return mn


S = Solution()
A = [ 1, 4, 5, 8, 10 ]
B = [ 6, 9, 15 ]
C = [ 2, 3, 6, 6 ]

print (S.solve(A,B,C))

'''


Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]

Output:

1

Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.

'''
