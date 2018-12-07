from sys import stdin as si

class Solution:
    def mx(self, b,e):
        return max(self.ans, (b, e), key=lambda x: x[1] - x[0])
    def maxone(self, A, B):
        t = B
        self.ans=(0,0)
        i=j=0
        while j<len(A):
            #print(i,j)
            if A[j]==1:
                j+=1
            else:
                if B==0:
                    self.ans = self.mx(i, j - 1)
                    i=j=j+1
                    continue
                if t==0:
                    self.ans = self.mx(i,j-1)
                    t+=1
                    while i < len(A) and A[i]!=0:
                        i+=1
                    i+=1
                else:
                    if A[j]==0:
                        t-=1
                    j+=1
        if j>=len(A):    j=len(A)-1
        self.ans = self.mx(i,j)
        return self.ans

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        arr = list(map(int, si.readline().strip().split()))
        n = int(si.readline().strip())
        print(S.maxone(arr, n))