from sys import stdin as si
from collections import Counter as c
from functools import reduce


class Solution:

    def bazinga(self,a):
        lst, l = [], int('1'*len(str(a)))
        while a > 0:
            l = int(''.join([i if i<'1' else '1' for i in str(a)]))
            a -=l
            lst.append(l)
        print (len(lst))
        print (*lst)
        #return reduce(lambda x, y: str(x)+' '+str(y), lst) # use reduce


if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    #n,m = map(int,si.readline().strip().split())
    #m = list(map(int, si.readline().strip().split()))
    n = int(si.readline().strip())
    S = Solution()
    S.bazinga(n)


'''
http://codeforces.com/contest/538/problem/B
'''