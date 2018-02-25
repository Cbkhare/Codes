from sys import stdin as si
from collections import Counter as c


class Solution:

    def __init__(self):
        self.track = []

    def lovetriangle(self,m,i):

        if len(self.track)==2:
            if m[i] -1 == self.track[0]:
                print ('YES')
                exit(0)
            else:
                return

        else:
            self.track.append(i)
            self.lovetriangle(m,m[i]-1)
            self.track.pop(-1)








if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n = si.readline().strip()
    m = list(map(int, si.readline().strip().split()))
    S = Solution()
    for i in range(len(m)):
        S.lovetriangle(m,i)
    else:
        print ('NO')


'''
http://codeforces.com/contest/939/problem/A
'''