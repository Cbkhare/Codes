from heapq import _heapify_max as hmax, _heappop_max as hpop
class Solution:
    def solve(self, A, B):
        hmax(A)
        hmax(B)
        res = []
        cout = 0
        a = b = None
        while cout<len(A):
            if not a and not b:
                a, b = hpop(A), hpop(B)
            elif not a and b:
                a = hpop(A)
            elif not b and a:
                b = hpop(B)
            res.append(a+b)
            if a>=b:
                b= None
            else:
                a= None
            cout +=1
        return res

s= Solution()
