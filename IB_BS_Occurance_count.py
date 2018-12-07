from sys import stdin as si


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        i = 0
        j = len(A)-1
        s = e = None
        found = False
        # find the start
        while i <= j:
            mid = i + (j - i) // 2
            prev = mid - 1

            #print ('1',i,j,mid,prev)
            if A[mid] == B:
                if prev == -1 or A[mid] != A[prev]:
                    s = mid
                    found = True
                    break
                if A[mid] == A[prev]:
                    j = mid-1
            elif B > A[mid]:
                i = mid + 1
            elif B <= A[mid]:
                j = mid -1

        if not found:
            return 0
        # Find the end
        i = 0
        j=len(A)-1
        while i <= j:
            mid = i + (j - i) // 2
            next = mid + 1
            #print ('2',i,j,mid,next)
            if A[mid] == B:
                if next == len(A) or A[mid] != A[next]:
                    e=mid
                    break
                if A[mid] == A[next]:
                    i = mid+1
            elif B >= A[mid]:
                i = mid +1
            # opposite of above loop
            elif B < A[mid]:
                j = mid - 1
        #print(e,s)
        return e-s+1

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        n = int(si.readline().strip())
        M = list(map(int, si.readline().strip().split()))
        print (S.findCount(M,n))
