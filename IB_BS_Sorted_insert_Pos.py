from sys import  stdin as si

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        li = len(A)-1
        i = 0
        j = li
        while i<=j:
            #print (i,j)
            mid = i + (j-i)//2

            if B==A[mid]:
                return mid
            prev =  mid-1
            next = mid+1
            #print (prev, next)
            if prev==-1:
                return 0
            elif next == li+1:
                return li +1
            if A[prev]<B<A[mid]:
                return mid
            elif A[mid]<B<A[next]:
                return mid+1
            elif B>A[mid]:
                i=mid+1
            elif B<A[mid]:
                j=mid
        return 0

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        b = int(si.readline().strip())
        arr = list(map(int, si.readline().strip().split()))
        print(S.searchInsert(arr,b))