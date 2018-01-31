from sys import stdin as si
from collections import Counter as c


class Solution:

    def bazinga(self,a,b):
        s =(b*(b+1)/2 - a)
        if s%2 !=0 : return ("impossible")
        target_sum = int(s/2)
        x = [0 for i in range(b)]
        x[a-1] = 2
        if a == 1:   # to avoid to zeorth index
            index1 = a
        else:
            index1 = a-2
        #print (x,index1, target_sum)
        x[index1] = x[target_sum - index1 - 2 ] = 1
        return ''.join(map(str,x))


if __name__ == '__main__':
    for i in range(int(si.readline().strip())):
        n,m = map(int, si.readline().strip().split())
        S = Solution()
        print(S.bazinga(n, m))


'''
https://www.codechef.com/JAN18/problems/PRTITION
    '''