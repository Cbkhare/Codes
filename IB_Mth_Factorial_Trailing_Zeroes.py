from sys import stdin as si

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        A5= A
        c5 =0
        while A5/5>0:
            c5+=A5//5
            A5//=5
        return c5


if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        print (S.trailingZeroes(int(si.readline().strip())))