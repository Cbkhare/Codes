from sys import stdin as si

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        mn_stack = [A[0]]
        mnl = [-1]
        for i in range(1,len(A)):
            if A[i]<=mn_stack[-1]:
                # keep on poping till you find less
                while mn_stack!= [] and A[i]<=mn_stack[-1]:
                    mn_stack.pop()
                if mn_stack==[]: mn_stack=[-1]
            mnl.append(mn_stack[-1])
            mn_stack.append(A[i])
        return mnl

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        arr = list(map(int, si.readline().strip().split(', ')))
        print(S.prevSmaller(arr))