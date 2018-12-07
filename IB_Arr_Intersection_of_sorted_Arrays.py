class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        i,j=0,0
        la,lb=len(A),len(B)
        if 0 in [la,lb]: return []
        f = []
        count = la+lb
        while i < la or j < lb:
            a, b = A[i], B[j]
            if a == b:
                f.append(a)
                if i < la - 1:
                    i += 1
                else:
                    break
                if j < lb - 1:
                    j += 1
                else:
                    break
                count -= 2
            else:
                mi = min(a, b)
                if mi == a:
                    if i < la - 1:
                        i += 1
                    else:
                        break
                if mi == b:
                    if j < lb - 1:
                        j += 1
                    else:
                        break
                        # count-=1
            if count <= 0:    break
        return f
    
S = Solution()
A = [ 1, 4, 6, 8, 9, 9, 10 ]
B = [ 6, 9, 9, 15 ]

print (S.intersect(A,B))

'''
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]

'''

