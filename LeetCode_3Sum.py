from sys import stdin as si

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        l = len(nums)
        print(l)
        if l <=2:   return []
        stack = []
        for i in range(l):
            j = i+1
            k = l-1
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in stack:
                        stack.append(triplet)

                if s >= 0:
                    k -= 1
                else:
                    j += 1
            return stack

if __name__=="__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        t = list(map(int, si.readline().strip().split(",")))
        print(S.threeSum(t))
