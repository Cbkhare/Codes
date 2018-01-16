from sys import stdin as si

if __name__== "__main__":
    n = int(si.readline())
    for j in range(n):
        m, k =  map(int,si.readline().split())
        lst = list(map(int, si.readline().split()))
        c = 0
        for i in lst:
            if (i+k)%7==0: c+=1
        print (c)