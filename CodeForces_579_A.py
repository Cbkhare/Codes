from sys import stdin as si
from collections import Counter as c
from functools import reduce


class Solution:

    def bazinga(self,a):
        c, tar= 0, True
        while a>1:
            b = bin(a)[2:]
            l = len(b)
            m = 1<<l-1
            a = a - m
            c+=1
        if a==1:    c+=1
        return c



if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    #n,m = map(int,si.readline().strip().split())
    #m = list(map(int, si.readline().strip().split()))
    n = int(si.readline().strip())
    S = Solution()
    print (S.bazinga(n))


'''
http://codeforces.com/contest/579/problem/A
'''