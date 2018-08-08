from sys import stdin as si
from heapq import heappop as hpop, heappush as hpush, heapify as hi

class Solution:

    def nthUglyNumber(self, x):
        #d = {1}    #either use set or diticonary (200ms vs 196 ms)
        d = {1:1}
        n = [1]
        hi(n)
        while True:
            l = hpop(n) # get lowest value in the set
            x -= 1
            if x==0:
                return l

            l2,l3,l5=l*2,l*3,l*5
            if l2 not in d:
                #d.add(l2)
                d[l2] =1
                hpush(n,l2)
            if l3 not in d:
                #d.add(l3)
                d[l3]=1
                hpush(n,l3)
            if l5 not in d:
                #d.add(l5)
                d[l5]=1
                hpush(n,l5)



if __name__=="__main__":
    for i in range(int(si.readline().strip())):
        S = Solution()
        print (S.nthUglyNumber(int(si.readline().strip())))

'''
This question is more about operlapping subrpoblem
like 3*2, 2*3, 3*5, 5*3
hence use a set or dict (follow commented text for set)

optimal substructure
for every min value perform l*2,l*3,l*5
To figure out it was solved, write ugly number upto 20 and see relation
between current number with earlier number'''