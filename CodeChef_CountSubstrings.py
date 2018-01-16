from sys import stdin as si
from math import factorial as f, floor as fl


if __name__=='__main__':
    n = int(input())
    for i in range(n):
        m = map(int, input())
        total = sum(list(map(int, input().split())))
        print(total + fl(total*(total-1)/2))
        #print (fl(total*(total+1)/2))


'''
https://www.codechef.com/problems/CSUB
'''
