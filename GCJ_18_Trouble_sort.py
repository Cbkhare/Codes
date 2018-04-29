from sys import stdin as si
from collections import Counter as c


class Solution:

    def bazinga(self, n, m):
        ei = sorted([ m[i] for i in range(0,n,2)])
        oi = sorted([ m[i] for i in range(1,n,2)])
        for i in range(n-1):
            #print (i,i//2)
            if i%2==0:
                if ei[i//2] > oi[i//2]:   return i  #ei[i]<=oi[i]
            else:
                if ei[(i//2)+1] < oi[i//2]:   return i  #ei[i+1]>=oi[i]
        return 'OK'


if __name__ == '__main__':
    for i in range(int(si.readline().strip())):
        #n = si.readline().strip().split()
        n = int(si.readline().strip())
        m = list(map(int, si.readline().strip().split()))
        S = Solution()
        print('Case #%d: %s' % (i+1, S.bazinga(n,m)))
