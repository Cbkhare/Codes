from sys import stdin as si
from collections import Counter as c


class Solution:


    def bazinga(self,b):
        a =1
        for i in range(2,int(b/2)+1):
            if (b-i)%i==0:  a+=1
        return a


if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n = int(si.readline().strip())
    #m = list(map(int, si.readline().strip().split()))
    S = Solution()
    print(S.bazinga(n))


'''
http://codeforces.com/contest/935/problem/A
'''