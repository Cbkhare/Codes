from sys import stdin as si
from collections import Counter as c


class Solution:


    def bazinga(self,a,b,c):

        for i in range(b):
            d = list(map(int, si.readline().strip().split()))
            if d[0]==1:
                c[d[1]-1] = d[2]
            else:
                p = 0
                if d[2]-d[1]+1<3:     print(0);continue
                x = sorted(c[d[1]-1:d[2]])
                for j in range(len(x)-1,1,-1):
                    #print (x, x[j-2:j+1])
                    if x[j-2]+x[j-1]>x[j]:
                        p = max(sum(x[j-2:j+1]),p)
                        if p>0: break
                print (p)

if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n,m = map(int, si.readline().strip().split())
    x = list(map(int, si.readline().strip().split()))
    S = Solution()
    #print(S.bazinga(n, m, x))
    S.bazinga(n, m, x)


'''
https://www.codechef.com/MARCH18B/problems/PSHTRG
'''