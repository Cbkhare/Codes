from sys import stdin as si
from functools import cmp_to_key

class Solution:

    def largestNumber(self, A):
        if len(A) == A.count(0): return 0
        def my_cmp(x,y):
            if int(x+y) > int(y+x):
                return -1
            elif int(x+y) > int(y+x):
                return 0
            else:
                return 1
        A = list(map(str, A))
        
        cmp = cmp_to_key(my_cmp) # sorted(A, cmp=..) cmp argument is dep in py 3.x
        A = sorted(A, key=cmp)
        #print (A)
        return ''.join(A)

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        print (S.largestNumber(list(map(int,si.readline().strip().split()))))