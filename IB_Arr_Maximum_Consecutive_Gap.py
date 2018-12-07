from sys import stdin as si
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        # Via HEAP,
        from heapq import heapify as hy, heappop as hp
        l = len(A)
        A = list(A)
        hy(A) #This step takes
        diff, old = 0, hp(A)
        for i in range(1, l):
            current = hp(A)
            diff = max(diff, current - old)
            old = current
        return diff

if __name__=="__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        print(S.maximumGap(tuple(map(int, si.readline().strip().split()))))