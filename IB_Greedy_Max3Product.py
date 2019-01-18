class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort()
        x = A[0]*A[1]
        y = A[-2]*A[-1]
        from sys import maxsize as m
        mx = x  * -m if x>0 else x*m
        for i in range(2,len(A)):
            mx = max(mx,x*A[i])
        my = y *-m if y>0 else y*m
        for i in range(0,len(A)-2):
            my = max(my,y*A[i])
        return max(mx,my)