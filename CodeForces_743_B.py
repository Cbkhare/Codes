from sys import stdin as si
from collections import Counter as c
from functools import reduce


class Solution:

    def bazinga(self,x,a):
        if a==1:    return 1
        while a>=1:
            l = len(bin(a)[2:])-1
            m = 1<<l
            #print (a,m)
            a = abs(a - m)
        if a==0:    l+=1
        return l



if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    #n,m = map(int,si.readline().strip().split())
    #m = list(map(int, si.readline().strip().split()))
    n, m = map(int,si.readline().strip().split())
    S = Solution()
    print (S.bazinga(n, m))

'''
http://codeforces.com/problemset/problem/743/B
'''