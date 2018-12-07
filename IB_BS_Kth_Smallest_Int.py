from sys import stdin as si

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def toing(self, A, B,t):
        count = 0
        for i in range(len(A)):
            if A[i]<=t:
                count+=1
                if count==B:
                    return 1
        return 0

    def kthsmallest(self, A, B):
        i = min(A)
        j = max(A)
        res = 0
        while i <= j:
            mid = i + (j - i) // 2
            print (i,j, mid)
            if self.toing(A, B, mid):
                res = mid
                j = mid - 1
            else:
                i = mid + 1
        return res

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        b = int(si.readline().strip())
        arr = list(map(int, si.readline().strip().split()))
        print(S.kthsmallest(arr,b))