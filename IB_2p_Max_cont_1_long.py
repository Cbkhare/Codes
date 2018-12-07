class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
    def maxone(self, A, B):
        b,e=0,0
        ans = (0,0)
        i=0
        l = len(A)
        c = B
        z = [i for i in range(len(A)) if A[i]==0]
        while i<l:
            if A[i]==1:
                e+=1
            else:
                if B==0:
                    ans = max(ans, (b, e), key=lambda x: x[1] - x[0])
                    b=e=i+1
                else:
                    if c==0:
                        #print (ans, b,e)
                        ans = max(ans, (b,e), key=lambda x: x[1]-x[0])
                        c = c + 1
                        b = z.pop(0)+1
                        e=i
                        c-=1
                        e+=1
                    else:
                        c-=1
                        e+=1
            i+=1
        ans = max(ans, (b,e), key=lambda x: x[1]-x[0])
        return list(range(ans[0],ans[1]))