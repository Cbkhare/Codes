from sys import stdin as si

class Solution:
    def maxone(self, A, B):
        b,e=0,0
        ans = (0,0)
        i=0
        l = len(A)
        c = B
        z = [i for i in range(len(A)) if A[i] == 0]
        while i<l:
            if A[i]==1:
                e+=1
            else:
                if B==0:
                    # take this index as hurdle and calculate values after it
                    ans = max(ans, (b, e), key=lambda x: x[1] - x[0])
                    b=e=i+1
                else:
                    if c==0:
                        print (ans, b,e)
                        ans = max(ans, (b,e), key=lambda x: x[1]-x[0])
                        # Update C with 1
                        c +=1
                        # find the index which would be new beginning
                        b = z.pop(0) + 1
                        e=i
                        c-=1
                        e+=1
                    else:
                        c-=1
                        e+=1
            i+=1
        ans = max(ans, (b,e), key=lambda x: x[1]-x[0])
        return list(range(ans[0],ans[1]))



if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        lst = list(map(int, si.readline().strip().split(', ')))
        m = int(si.readline().strip())
        print(S.maxone(lst, m))