from sys import stdin as si

if __name__== "__main__":
    n = int(si.readline())
    for j in range(n):
        m = si.readline()
        lst = list(map(int, si.readline().split()))
        print (sum(lst) - len(lst) * min(lst))




'''
https://www.codechef.com/problems/SALARY
'''