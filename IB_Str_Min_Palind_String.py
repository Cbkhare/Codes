from sys import stdin as si

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        i,j=1,1
        while i<=len(A):
            # since element are to be only inserted at beginning, thus calc
            # max palind from beginning
            if A[:i]==A[:i][::-1]:
                j = max(j,i)
            i+=1
        t = len(A) - j
        #print (i,j,t)
        return t # t-1 if len(A)%2==0 else t


    def solve1(self, A):
        i,j=0,len(A)-1
        count = 0
        while i<=j:
            print (A[i], A[j], count)
            if A[i]==A[j]:
                i+=1
                j-=1
            else:
                j-=1
                count+=1
        return count

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        print(S.solve(si.readline().strip()))