
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        Min = None
        i, j, k = 0, 0, 0
        while i < len(A) and j < len(B) and k < len(C) :
            temp = max(A[i], B[j], C[k]) - min(A[i], B[j], C[k])
            if Min == None or temp < Min :
                Min = temp
            if temp == 0 :
                break
            if min(A[i], B[j], C[k]) == A[i]:
                i += 1
            elif min(A[i], B[j], C[k]) == B[j] :
                j += 1
            else :
                k += 1
        return Min

'''


You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;

Example :

Input : 
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]

Output : 5 
         With 10 from A, 15 from B and 10 from C. 

'''