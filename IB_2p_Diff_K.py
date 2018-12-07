from sys import stdin as si
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A)<=1:   return  0
        i,j=0,1
        while i<len(A) and j<len(A):
            print(len(A),i,j, A[i],A[j])
            if i==j:
                j+=1
                continue
            a,b =A[i], A[j]
            diff = abs(b-a)
            if diff==B:
                return 1
            elif diff<B:
                j+=1
            else:
                i+=1
        return 0



if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        lst = list(map(int, si.readline().strip().split(', ')))
        m = int(si.readline().strip())
        print(S.diffPossible(lst, m))

