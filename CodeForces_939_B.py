from sys import stdin as si
from collections import Counter as c


class Solution:

    def bazinga(self, n,m):
        if n==0:    return '1 0'
        l,b = n, 0
        ans = [1,b]
        for i in range(len(m)):
            bb = n//m[i]
            ll = n%m[i]
            if ll < l:
                ans[0] = i+1
                ans[1] = bb
                l,b =ll, bb
            elif ll==l:
                if ans[1] < bb:
                    ans[0] = i+1
                    ans[1] = bb
                    l, b = ll, bb

        return ' '.join(map(str,ans))


if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n, k = map(int, si.readline().strip().split())
    m = list(map(int, si.readline().strip().split()))
    S = Solution()
    print(S.bazinga(n, m))

'''
http://codeforces.com/contest/939/problem/C
'''