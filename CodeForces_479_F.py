from sys import stdin as si
from sys import maxsize as m
from collections import Counter as C
from operator import  itemgetter as ig
from functools import reduce

class Solution:

    def bazinga1(self, k,t):
        st = sorted(list(enumerate(t)), key=ig(1))
        stack = []
        temp  = [st[0][0]]
        print(st)
        for i in range(1,len(st)):
            print (temp)
            if st[i][1] == t[temp[-1]]: #continue #temp.pop(-1)
                temp.append(min(st[i][0],temp[-1]))
                temp.pop(-2)
                continue
            if st[i][0] > temp[-1] and st[i][1] == t[temp[-1]]+1:         #index of larger value is at larger index
                temp.append(st[i][0])
            else:
                if len(temp)>= len(stack):   stack=temp[::]
                temp=[st[i][0]]
        if len(temp) >= len(stack):  stack = temp[::]
        print (len(stack))
        #if len(stack)==1:   print(st)
        stack = [1+x for x in stack]
        print (*stack)

    def bazinga2(self, k, t):
        d = {}
        for i in range(len(t)):
            d[t[i]] = d.get(t[i], []) + [i]
        self.sd = sorted(d.items())  #sorted(d.items(), key= lambda x : x[1])
        del d
        self.g = t
        l =len(self.sd)
        #print (self.sd)
        self.temp = []
        self.bazinga2(0,l)
        stack = reduce(lambda x,y: x if len(x) > len(y) else y, self.temp)
        print (len(stack))
        stack = [1 + x for x in stack]
        print(*stack)


    def bazinga21(self,i, l, sdi=None):
        t = []
        if i==l-1:
            for j in self.sd[l-1][1]:
                if self.g[sdi]+1 == self.g[j]:
                    t.append([j])
            if t!=[]:   self.temp.extend(t)
        else:
            b = []
            for j in self.sd[i][1]:
                #print(self.temp, i, sdi)
                self.bazinga2(i+1,l,j)
                for t in self.temp:
                    if self.g[t[0]] == 1+ self.g[j] and t[0] > j:
                        t.insert(0,j)
                b.append([j])
            self.temp.extend(b)
            #print ('second', self.temp)


    def bazinga(self, n,l):
        lnt,lst_elmnt = 0,0
        dp = {}
        for i in range(n):
            dp[l[i]] = dp.get(l[i]-1,0) + 1
            if lnt < dp[l[i]]:
                lnt = dp[l[i]]
                lst_elmnt = l[i]
        ans = []
        for i in range(n-1,-1,-1):
            if l[i] == lst_elmnt:
                ans.append(i)
                lst_elmnt-=1
        print (lnt)
        ans = [1+j for j in ans[::-1]]
        print (*ans)

if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n = int(si.readline().strip())
    #m,n = map(int,si.readline().strip().split())
    #t = C(tuple(map(int,si.readline().strip().split())))
    l = list(map(int, si.readline().strip().split()))
    S = Solution()
    S.bazinga(n,l)
