from sys import stdin as si

def candies(n, A):
    if len(A)==1:   return 1
    t =[1]*len(A)
    for i in range(1,n):  # for ascending
        if A[i]>A[i-1]:
            t[i] += t[i-1]

    for i in range(n-2,0,-1): # for descending
        if A[i]>A[i+1]:
            t[i] = max(t[i+1]+1,t[i])
    return sum(t)

if __name__=="__main__":
    x = list(map(int, si.readline().strip().split()))
    print (candies(len(x), x))

'''
Observe the series in form of ascending and descending
3 4 5 4 2 1
'''