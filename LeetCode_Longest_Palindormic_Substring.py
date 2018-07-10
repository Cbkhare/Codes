from sys import  stdin as si
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.bazinga(s,0, len(s)-1)

    def bazinga(self, s,b,e):
        if b==e:
            pass
        if s[b] == s[e]:
            self.bazinga(s, b+1, e-1)
        else:
            max(self.bazinga(s, b, e-1), self.bazinga(s,b+1,e),
                key=lambda x: len(x))

if __name__=="__main__":
    for i in range(int(si.readline().strip())):
        S = Solution()
        print (S.longestPalindrome(si.readline().strip()))
