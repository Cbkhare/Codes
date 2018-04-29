#from sys import stdin as si
#from collections import Counter as c


class Solution:


    def bazinga(self,b):
        #return max(int(b/10), int(b/100)+ pow(10,len(str(int(b/100))))*(b%10)*-1 if b<0 else 1,b)
        #print (b, int(str(b)[:-1]), int(str(b)[:-2]+str(b)[-1]))
        return (max(b, int(str(b)[:-1]), int(str(b)[:-2]+str(b)[-1])))


if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    #n,m = map(int,si.readline().strip().split())
    #m = list(map(int, si.readline().strip().split()))
    n = int(input().strip())
    S = Solution()
    print(S.bazinga(n))


'''
http://codeforces.com/contest/276/problem/D
'''