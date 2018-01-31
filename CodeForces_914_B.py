from sys import stdin as si
from collections import Counter as c
from operator import itemgetter as ig


class Solution:
    def bazinga(self,b):
        b = c(b)
        b = sorted(b.items() , key=ig(0), reverse=True)
        for i in b:
            if i[1]%2 !=0:  return 'Conan'
        else:
            return 'Agasa'



if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n = si.readline().strip()
    m = map(int, si.readline().strip().split())
    S = Solution()
    print(S.bazinga( m))

'''
http://codeforces.com/contest/914/problem/B
    '''