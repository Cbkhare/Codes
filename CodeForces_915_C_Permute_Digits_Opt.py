from sys import stdin as si
from collections import Counter as c


class Solution:

    def bazinga(self,feq, m, ct, down, ans):
        if ct == len(m):
            print (ans)
            exit(0)
        if down:
            begin_with = 9
        else:
            begin_with = int(m[ct])

        for i in range(begin_with, -1, -1):
            i = str(i)
            if i in feq and feq[i] > 0:
                feq[i] -= 1
                if int(i) != begin_with: down=1
                got = self.bazinga(feq, m, ct+1, down, ans+i)
                if got: return
                feq[i] += 1


    def precompute_digits(self,n, m):
        if len(n) < len(m):
            print (''.join(sorted(n, reverse=True)))
            return
        feq = c(n)
        count, down = 0, False
        self.bazinga(feq, m, count, down, '')
        return

    def precomp_dig(self,a, b):
        a = sorted(a)
        r, p = range(len(a)), lambda x: int(''.join(x))
        for i in r:
            for j in r[i:]:
                a[i], a[j], c = a[j], a[i], p(a)
                if not (c <= p(a) <= p(b)):
                    a[i], a[j] = a[j], a[i]
        print(p(a))
        return

if __name__=='__main__':
    #for i in range(int(si.readline().strip())):
    n = si.readline().strip()
    m = si.readline().strip()
    S = Solution()
    S.precompute_digits(n,m)
    #S.precomp_dig(n,m)


'''
123456789123456789
276193619183618162
'''