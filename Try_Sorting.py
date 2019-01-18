from sys import stdin as si

class Sort:

    def __init__(self):
        pass

    def insertion_sort(self,A):
        for i in range(1,len(A)):
            j = i-1
            while j>0 and A[j]>A[i]:
                A[j],A[i]= A[i],A[j]
                j-=1
                i-=1
        return A



if __name__=="__main__":
    for _ in range(int(si.readline().strip())):
        S = Sort()
        array = list(map(int, si.readline().strip().split()))
        print (S.insertion_sort(array))
