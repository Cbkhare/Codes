from sys import stdin as si
from math import sqrt
from collections import Counter as c
import re

class Solution:

    def __init__(self):
        self.lst = []

    def is_prime(self, a):
        return all(a % i for i in range(2, int(a**.5)+1))

    def bazinga(self, m):
        if m==1 or (m > 1 and len(self.lst)==3):
            return False
        if m==0:
            print (len(self.lst))
            print (str(self.lst).replace(']','').replace('[','').replace(',',''))
            exit(0)

        for i in range(m,1,-1):
            if self.is_prime(i):
                self.lst.append(i)
                if not self.bazinga(m-i):
                    self.lst.pop(-1)




if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    m = int(si.readline().strip())
    S = Solution()
    S.bazinga(m)

'''
http://codeforces.com/contest/584/problem/D
'''