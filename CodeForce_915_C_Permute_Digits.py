from sys import stdin as si
from collections import Counter as c


class Solution:

    def bazinga(self,feq, m, ct):
        if ct == len(m):
            return
        elif ct == 0:
            t = m[:ct+1]
            self.bharo = [x for x in feq if x <= t]
            self.bazinga(feq, m, ct+1)
        else:
            t = m[:ct+1]
            temp = []
            for i in range(len(self.bharo)):
                feq_val = c(self.bharo[i])
                put_val, put_val_2 = '', ''
                for k,v in feq.items():
                    if k in feq_val and v <= feq_val[k]:
                        continue
                    put_val = k+self.bharo[i]
                    put_val_2 = self.bharo[i] + k
                    if put_val not in temp and put_val not in self.bharo and \
                            int(put_val) < int(t):
                        temp.append(put_val)
                    if put_val_2 not in temp and put_val_2 not in self.bharo \
                            and int(put_val_2) < int(t):
                        temp.append(put_val_2)
                #print ('sdsdsdsd', t, feq, feq_val, put_val, put_val_2)
            self.bharo = temp
            self.bazinga(feq, m, ct + 1)


    def precompute_digits(self,n, m):
        if len(n) < len(m):   return [''.join(sorted(n))]
        feq = c(n)
        count = 0
        self.bharo = []
        self.bazinga(feq, m, count)
        return self.bharo


if __name__=='__main__':
    #for i in range(int(si.readline().strip())):
    n = si.readline().strip()
    m = si.readline().strip()
    S = Solution()
    print (max(S.precompute_digits(n,m)))