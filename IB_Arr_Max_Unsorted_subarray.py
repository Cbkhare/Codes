from sys import stdin as si
from functools import cmp_to_key


#class Solution:
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort_mine(self, A):
        X = sorted(A)
        s, e = 0, 0
        for i in range(len(A)):
            if A[i] != X[i]:
                s = i
                break
        for i in range(len(A) - 1, -1, -1):
            if A[i] != X[i]:
                e = i
                break
        return [-1] if s == e == 0 else [s, e]

    def subUnsort(self, arr):
        # if the array has not at least 2 elemets it is sorted
        if len(arr) < 2:
            return -1

        # find the index of the last value
        # which is not larger than all previous elements
        right = None
        l_max = arr[0]
        i = 1
        while i < len(arr):
            if arr[i] < l_max:
                right = i
            else:
                l_max = arr[i]
            i += 1

        # if none exists the array is already sorted
        if not right:
            return [-1]

        # start from the identified index
        # and search for first value which is not smaller
        # than all the previous values
        left = right - 1
        r_min = arr[right]
        i = right - 1
        while i >= 0:
            if arr[i] > r_min:
                left = i
            else:
                r_min = arr[i]
            i -= 1

        # O_space ( 1 ), O_time( 2*N ) = O(N)
        return [left, right]


if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        print(S.subUnsort(list(map(int, si.readline().strip().split()))))