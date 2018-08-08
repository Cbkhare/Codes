class Solution:
    def __init__(self):
        self.d = {1: 1, 2: 2, 3: 3}

    def integerBreak1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.d:
            self.d[n] = max(self.integerBreak1(n - 3) * 3,
                            self.integerBreak1(n - 2) * 2)
        return self.d[n]

    def integerBreak(self, n):
        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            return self.integerBreak1(n)


'''
https://leetcode.com/problems/integer-break/description/
optimal substructure, find by comparing n=[7,10]
            self.d[n] = max(self.integerBreak1(n - 3) * 3,
                            self.integerBreak1(n - 2) * 2)
overlapping solution:- self.d
'''