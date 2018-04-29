from sys import stdin as si
from collections import Counter as c
from functools import reduce as r
from itertools import permutations as p

class Solution:

    def bazinga(self,a):
        l = len(str(a))
        if a >= int('7'*l) or l%2!=0:
            if l%2==0:  l+=2
            else:   l+=1
            print ('4'*(l//2)+'7'*(l//2))
            return
        elif a <= int('4'*l):
            if l%2!=0:  l+=1
            print('4' * (l // 2) + '7' * (l // 2))
            return
        #n = '4' * (l // 2) + '7' * (l // 2)
        #z = r(lambda x, y: y if ''.join(y) > ''.join(x) else x, p(n))
        z = '4' * (l // 2 +1) + '7' * (l // 2+1)

        for zz in p(n):
            if int(''.join(zz)) >= a:
                z=min(int(''.join(zz)),z)

        print (z)

if __name__ == '__main__':
    for i in range(int(si.readline().strip())):
    #n,m = map(int,si.readline().strip().split())
    #m = list(map(int, si.readline().strip().split()))
        n = int(si.readline().strip())
        S = Solution()
        S.bazinga(n)


'''
http://codeforces.com/contest/96/problem/B

n, b= [], 0
        c7,c4=0,0
        for i in str(a)[::-1]:
            if b:   i = str(int(i) + b)
            #print (i,n)
            if int(i) in range(5,8):
                n.append('7')
                c7+=1
            else:           # for i in range(1,5) (8,9)
                n.append('4')
                c4+=1

            if int(i)>7: b=1
            else:   b=0

        if b:   n.append('4');c4+=1
        if len(n)%2!=0: n.append('4');c4+=1
        #print (n)
        i = 0
        while c7!=c4 and i <len(n):
            if c7 < c4 and n[i] != '7':
                n[i] = '7'
                c7+=1
                c4-=1
            elif c7 > c4 and n[i] != '4':
                n[i] = '4'
                c4+=1
                c7-=1
            i+=1
        print (''.join((n[::-1])))
'''