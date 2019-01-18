class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        d = {0:-1}
        sum = 0
        mx_range = None
        for i in range(len(A)):
            sum += A[i]
            if sum in d:
                # this means sum has repeated which is only possible if
                # the sum in between is zero
                t = (d[sum]+1, i)
                if not mx_range:
                    mx_range = t
                else:
                    mx_range = max([mx_range,t], key=lambda x: x[1]-x[0])
            else:
                d[sum] = i
        #print (d,mx_range)
        if not mx_range:
            return []
        return A[mx_range[0]:mx_range[1]+1]