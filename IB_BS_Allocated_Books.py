from sys import  stdin as si

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def bs(self,A,B,dis):
        if dis<max(A):
            return 0
        count = 0
        crnt = 0
        for i in range(len(A)):
            nxt = A[i]
            if nxt + crnt <= dis:
                crnt+=nxt
            else:
                # when it became larger
                count += 1
                if count == B:
                    return 0
                crnt = nxt
        return 1

    def books(self, A, B):
        l = len(A)
        if B>l: return -1
        mn = min(A)
        op = l-B
        i = 0
        mx= 0
        while i+op<l:
            #print (i,op)
            mx=max(mx, sum(A[i:i+op+1]))
            i+=1
        res = -1
        while mn<=  mx:
            mid = mn + (mx-mn)//2
            #print(mn ,mx,mid)
            if self.bs(A,B,mid):
                res = mid
                mx = mid-1
            else:
                mn = mid+1
        return res

    def func(self, A1, B1, pgs1):
        if pgs1 < max(A1):
            return 0
        cur_sum1 = 0
        c1 = 0
        for pg1 in A1:
            if cur_sum1 + pg1 <= pgs1:
                cur_sum1 += pg1
            else:
                c1 += 1
                if c1 >= B1:
                    return 0
                cur_sum1 = pg1
        return 1

    def books_ref(self, A1, B1):
        if len(A1) < B1:
            return -1
        low1 = min(A1)
        high1 = sum(A1)
        res1 = -1
        while low1 <= high1:
            mid1 = int((low1 + high1) / 2)
            t1 = self.func(A1, B1, mid1)
            if t1:
                res1 = mid1
                high1 = mid1 - 1
            else:
                low1 = mid1 + 1
        return res1


if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        arr = list(map(int, si.readline().strip().split(', ')))
        b = int(si.readline().strip())
        print(S.books(arr,b))