from sys import stdin as si
from collections import Counter as c


class Solution:

    def bazinga(self, d, S):

        pd, cd, c,s =0,1,0,0
        for i in S:
            if i=='C':
                c+=1
                cd = 1<<c
            if i=='S':
                pd+=cd

        if pd<d:    return '0'
        else:
            i=len(S)-1
            while pd >d and i>0:
                if S[i]=='S' and S[i-1]=='C':
                    S[i],S[i-1] = S[i-1],S[i]
                    i+=1
                    if i ==len(S):  i-=1
                    s+=1
                    if c<=0:    break
                    pd-=1<<c
                    pd+=1<<(c-1)
                else:
                    if S[i]=='C':  c-=1;S[i]='VC'  #visited C
                    i-=1

                #print (S,pd,d,s,c)
            if pd<=d:    return  str(s)
            else:   return 'IMPOSSIBLE'


if __name__ == '__main__':
    for i in range(int(si.readline().strip())):
        n,m = si.readline().strip().split()
        #m = list(map(int, si.readline().strip().split()))
        S = Solution()
        print('Case #%d: %s' % (i+1, S.bazinga(int(n),list(m))))
