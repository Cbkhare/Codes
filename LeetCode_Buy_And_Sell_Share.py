class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices == []:    return 0
        diff = 0
        mn = prices[0]
        for i in prices[1:]:
            if i < mn:
                mn = i
            else:
                diff = max(diff, i - mn)
        return diff


'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Find the maximum difference between two numbers in the list such that the 
larger number is always after the smallest number'''