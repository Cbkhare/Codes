from sys import stdin as si

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        for i in range(len(A)):
            v = A[i]
            index = None
            if v < 0:
                index = -1*v
            else:
                index = v
            index -= 1 # since zero based array
            if A[index]<0:
                return index + 1
            else:
                A[index] *= -1 # visited
        return -1



if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        print(S.repeatedNumber(list(map(int, si.readline().strip().split()))))

