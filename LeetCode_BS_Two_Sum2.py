from sys import stdin as si

class Solution:

    def find_bs(self, A, X, n):
        i = 0
        j = len(A) - 1
        while i <= j:
            m = i + (j - i) // 2
            if A[m] == X and m!=n:
                return m
            elif A[m] <= X:
                i = m + 1
            elif A[m] > X:
                j = m - 1
        return -1

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            f = target - numbers[i]
            v = self.find_bs(numbers, f, i)
            if v>=0:
                return i+1, v+1

    def twoSum_2pointers(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            temp = numbers[i] + numbers[j]
            if temp == target:
                return [i + 1, j + 1]
            else:
                if temp > target:
                    j = j - 1
                else:
                    i = i + 1

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        b = int(si.readline().strip())
        arr = list(map(int, si.readline().strip().split()))
        print(S.twoSum(arr,b))