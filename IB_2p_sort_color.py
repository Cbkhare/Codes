class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        #return sorted(A)
        mp = {0:0,1:0,2:0}
        for c in A:
            mp[c] += 1
        return mp[0]*[0] + mp[1]*[1] + mp[2]*[2]