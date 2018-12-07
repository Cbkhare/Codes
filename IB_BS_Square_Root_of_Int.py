from sys import  stdin as si

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A<=1:    return A
        i=1
        j=A//2
        while i<=j:
            mid = i+(j-i)//2
            if mid*mid<=A<(mid+1)*(mid+1):
                return mid
            elif A<mid*mid:
                j=mid
            elif A>mid*mid:
                i=mid+1


if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        #lst = list(map(int, si.readline().strip().split(', ')))
        m = int(si.readline().strip())
        print(S.sqrt(m))