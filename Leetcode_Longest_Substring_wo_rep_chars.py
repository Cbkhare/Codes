from sys import stdin as si

class Solution:
    def lengthOfLongestSubstring(self, s):
        # 736 ms
        """
        :type s: str
        :rtype: int
        """
        h = {}
        i = 0
        c = 0
        cc = 0
        while i < len(s):
            if s[i] not in h:
                h[s[i]] = i
                cc += 1
                i += 1
            else:
                i = h[s[i]] + 1
                h = {}

                c = max(cc, c)
                cc = 0

        c = max(cc, c)
        return c

    def lengthOfLongestSubstring1(self, s):
        # 152 ms
        """
        :type s: str
        :rtype: int
        """
        h = {}
        i = 0
        c = 0
        cc = 0
        t = -1
        while i < len(s):
            if s[i] not in h or h[s[i]]<t:
                cc += 1
            else:
                cc = i - h[s[i]]
                t = h[s[i]]
            h[s[i]] = i
            i+=1
            c = max(cc, c)
        return c

    def lengthOfLongestSubstring2(self, s):
        # 128 ms
        """
        :type s: str
        :rtype: int
        """
        h = {}
        i = 0
        c = 0
        cc = 0
        t = -1
        for i in range(len(s)):
            p = h.get(s[i],None)
            if s[i] not in h or p<t:
                cc += 1
            else:
                cc = i - p
                t = p
            h[s[i]] = i
            c = max(cc, c)
        return c

if __name__=="__main__":
    for _ in range(int(si.readline().strip())):
        x = si.readline().strip()
        S = Solution()
        print (S.lengthOfLongestSubstring1(x))


'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''