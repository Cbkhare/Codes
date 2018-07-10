class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.d = {} # for each number there is a list of numbers divisible by that number
        self.nums = sorted(nums)
        self.l = len(self.nums)
        m_ans = ()
        for i in range(len(self.nums)):
            m_ans = max(self.solve(i), m_ans, key=len)
        return m_ans


    def solve(self, i):
        if i >= self.l: return set()
        if i in self.d: return self.d[i]
        m_out = ()
        for j in range(i+1):
            if self.nums[j+i]%self.nums[i]==0:
                out = self.solve(j+i) |{self.nums[j+i]}
                m_out = max(out, m_out, key=len)
        self.d[i] = m_out
        return self.d[i]


'''
https://leetcode.com/problems/largest-divisible-subset/description/

Optimal Substructure:-
[a,b,c,d,e]

Predicate:- if b is divisible by a then every value divisivle by b is also divisible by a.
Iterate over each value in the list. For each value check the divisibility against 
other numbers. 
And for each divisible numbers follow the predicate.
 
overlapping Solution:-
Use self.d, for most of the numbers the check during divisibility will be resolved
and recheck are line no.12 wont be reuqired.


a faster sol
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))
'''