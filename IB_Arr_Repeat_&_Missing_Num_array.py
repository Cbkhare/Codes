from sys import stdin as si

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        l = len(A)
        s = sum(A)
        sn = sum(range(1,l+1))
        d = sn - s
        s2,sn2=0,0
        for i in range(len(A)):
            s2 += (A[i]**2)
            sn2 += ((i+1)**2)
        sd = sn2-s2
        m = (sd + d**2)//(2*d)
        r = m-d
        return m,r


if __name__=="__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        print(S.repeatedNumber(tuple(map(int, si.readline().strip().split()))))

'''
Find the missing and repeating number'''