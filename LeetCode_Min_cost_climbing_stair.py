class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        self.cost = cost
        self.d = {}
        self.l = len(self.cost)
        return min(self.solve(0), self.solve(1))

    def solve(self, n):
        if n in self.d: return self.d[n]
        if n >= self.l:  return 0
        if n == self.l - 1 or n == self.l - 2:
            return self.cost[n]
        else:
            out = self.cost[n] + min(self.solve(n+1), self.solve(n+2))
        self.d[n] = out
        return self.d[n]

'''
https://leetcode.com/problems/min-cost-climbing-stairs/description/

Optimal Substructure:- 
min(self.solve(n+1), self.solve(n+2))

Overlapping solution: 
self.d 

Similar to house robbery
'''