class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        self.d = {}
        return max(self.solve(0), self.solve(1))

    def solve(self, n):
        if n >= len(self.nums):   return 0
        if n in self.d: return self.d[n]
        if n in [len(self.nums) - 1, len(self.nums) - 2]:
            return self.nums[n]
        else:
            out = self.nums[n] + max(self.solve(n + 2), self.solve(n + 3))
        self.d[n] = out
        return self.d[n]

'''
https://leetcode.com/problems/house-robber/description/

Optimal substructure:-
For all n+2, n+3 -> is true is also true for n, hence max(n+2,n+3)

Overlapping subsolution
use self.d = {}:- '''