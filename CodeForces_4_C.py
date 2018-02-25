from sys import stdin as si
from collections import Counter as c


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):    return False
        cms = {}
        cmt = {}
        for i in range(len(s)):
            if s[i] not in cms and t[i] not in cmt:
                cms[s[i]] = [i]
                cmt[t[i]] = [i]
            elif s[i] in cms and t[i] in cmt:
                if sorted(cms[s[i]]) != sorted(cmt[t[i]]):
                    return False
                else:
                    cms[s[i]].append(i)
                    cmt[t[i]].append(i)
            else:
                return False
        return True

if __name__ == '__main__':
    pass
