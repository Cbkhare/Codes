class Solution:

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        d = [0]
        for i in range(1,num+1):
            x = d[i//2] if i%2==0 else d[i//2]+1 # think this form left and right shift operation
            d.append(x)
        return d

'''
https://leetcode.com/problems/counting-bits/description/
overlapping substructure
bits in odd number = number of bits in (x>>1) + 1
and 
bits in even number = number of bits in (x>>1)
'''