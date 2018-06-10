from sys import stdin as si
from collections import Counter as C


class Solution:
    def bazinga(self, s, k,t):
        n=1
        ck = False
        st = sorted(t.items())
        if k==0:
            if st[0][0]==1: return -1
            else:   return st[0][0]-1


        for i in range(len(st)):
            n = st[i][0]
            k-=st[i][1]
            if k==0:    return n
            if k<0:
                return -1

if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    m,n = map(int,si.readline().strip().split())
    t = C(tuple(map(int,si.readline().strip().split())))
    S = Solution()
    print (S.bazinga(m,n,t))