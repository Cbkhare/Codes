from sys import stdin as si
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        stack = []
        ans = []
        for i in range(len(A) - 1, -1, -1):
            found = False
            while stack != []:
                if stack[-1] > A[i]:
                    ans.append(stack[-1])
                    found = True
                    break
                stack.pop(-1)
            if not found: ans.append(-1)
            stack.append(A[i])
        return ans[::-1]



if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        M = list(map(int, si.readline().strip().split()))
        print(S.nextGreater(M))

'''
https://www.interviewbit.com/problems/nextgreater/
'''