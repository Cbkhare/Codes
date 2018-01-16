from sys import stdin as si

if __name__== "__main__":
    n = int(si.readline())
    for j in range(n):
        m = si.readline()
        lst = list(map(int, si.readline().split()))
        count = 0
        while min(lst) != max(lst):
            lst.sort()
            lst = lst[-1:-2:-1] + [x+1 for x in lst[:-1]]
            count += 1
        print(count)


'''
https://www.codechef.com/problems/SALARY
'''