from sys import stdin as si

class Solution:
    # @param A : list of strings
    # @return a strings
    def common(self, s1,s2):
        cm = ""
        l = min(len(s1), len(s2))
        for i in range(l):
            if s1[i]==s2[i]:
                cm+=s1[i]
            else:
                break
        return cm

    def longestCommonPrefix(self, A):
        l = len(A)
        if l == 1:  return A[0]
        i,pre = 1,""
        while i <len(A):
            cn = self.common(A[i],A[i-1])
            if cn=="":
                return ""
            A[i] = cn
            i+=1
        return A[-1]


if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        M = list(map(str, si.readline().strip().split()))
        print(S.longestCommonPrefix(M))