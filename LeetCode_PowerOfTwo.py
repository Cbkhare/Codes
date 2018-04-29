class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n!=0 and ((n-1) & (n) ==0))

# return if a number is power of two or not