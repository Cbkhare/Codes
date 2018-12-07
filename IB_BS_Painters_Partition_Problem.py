from sys import stdin as si

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def find_bs(self, tar,a,b,c):
        count = 1
        val = 0
        for i in range(len(c)):
            val += c[i]*b
            if val >tar:
                count+=1
                if count>a: return 0
                val = c[i]*b
            #print (val,count)
        return 1

    def paint1(self,A,B,C):
        mnt = max(C)*B
        mxt = sum(C)*B
        res = 0
        while mnt<=mxt:
            m = mnt + (mxt-mnt)//2
            t = self.find_bs(m,A,B,C)
            #print (m,t,mxt,mnt)
            if t:
                res = m
                mxt = m -1
            else:
                mnt = m + 1
        return res % 10000003

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        a = int(si.readline().strip())
        b = int(si.readline().strip())
        arr = list(map(int, si.readline().strip().split(', ')))
        print(S.paint1(a,b,arr))

'''
A : 5
B : 10
C : [ 658, 786, 531, 47, 169, 397, 914 ]'''