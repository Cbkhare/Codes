from sys import stdin as si
#from collections import Counter as c


class Solution:


    def bazinga1(self,a,b):
        if a==b:
            return 0
        z= lambda x:list(bin(x))[2:] ## z(a)
        ii = lambda x: int(''.join(x),2)
        a,b = z(a), z(b)
        #print (a,b)
        a = ['0']*(len(b)-len(a)) + a
        i = len(b)-1
        while i>0 :
            if a[i] == b[i]:    #set([a[i],b[i]]) != {'0','1'}:
                if a[i]=='0':
                    a[i]='1'  # only increase
                    if ii(a) >= ii(b):
                        a[i]='0';break
                else:
                    b[i]='0'  # only decrease
                    if ii(a) >= ii(b):
                        b[i]='1';break
            i-=1
        return ii(a)^ii(b)

    def bazinga(self,a,b):
        n = a^b
        a = 1
        while (n):
            a *=2
            n = int(n/2)
        return a-1

if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n,m = map(int,si.readline().strip().split())
    #m = list(map(int, si.readline().strip().split()))
    S = Solution()
    print(S.bazinga(n,m))


'''
http://codeforces.com/contest/276/problem/D
'''