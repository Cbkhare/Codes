from sys import stdin as si

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def toing(self, A, B,t):
        count = 0
        '''
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j]<=t:
                    count+=1
                    if count==B:
                        return 1
        return 0
        '''
        i = 0
        j = len(A[0])-1
        while i < len(A) and j>=0:
            if A[i][j] <= t:
                i +=1
                count += j+1
                if count >= B:
                    return 1
            else:
                j-=1
        return 0

    def kthSmallest(self, M, k):
        l = len(M)
        col = len(M[0])
        i = M[0][0] #min
        j = M[l-1][col-1]
        res = 0
        while i <= j:
            mid = i + (j - i) // 2
            #print (i,j, mid)
            if self.toing(M, k, mid):
                res = mid
                j = mid - 1
            else:
                i = mid + 1
        return res

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        matrix = [
                     [1, 5, 9],
                     [10, 11, 13],
                     [12, 13, 15]
                 ]
        b = int(si.readline().strip())
        print(S.kthSmallest(matrix,b))

'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/'''