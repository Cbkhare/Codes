from sys import stdin as si
from collections import Counter as c


class Solution:


    def bazinga(self,a,b,c):
        r = 0
        if a==0:    r = b;c=[b]
        elif a==1:    return (r,c)
        else:
            for i in range(1,a):
                z = max(0, b - c[i] - c[i-1])
                r +=z
                c[i] += z
        return (r,c)

if __name__ == '__main__':
    #for j in range(int(si.readline().strip())):
    n,m = map(int,si.readline().strip().split())
    x = list(map(int, si.readline().strip().split()))
    S = Solution()
    ans = S.bazinga(n,m,x)
    print (ans[0])
    print (str(ans[1]).replace('[','').replace(']','').replace(',',''))



'''
http://codeforces.com/contest/732/problem/B
'''