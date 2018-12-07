from sys import stdin as si

class Solution:

    def solve(self, A):
        A.sort()
        i, l = 0, len(A)
        while i<l:
            j = i+1
            while j<l and A[j] == A[i]:
                j += 1
                i += 1
            if l-i-1 == A[i]:
                return 1
            i += 1
        return -1

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        print (S.solve(list(map(int,si.readline().strip().split()))))
