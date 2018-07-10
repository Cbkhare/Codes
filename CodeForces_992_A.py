from sys import stdin as si

class Solution:
    def bazinga(self, b):
        c = 0
        t = 0
        for i in b:
            if i!=0:
                mz = -1*(i+c)
                c+=mz
                if mz!=0:
                    t+=1
        return t





if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n = si.readline().strip()
    m = map(int, si.readline().strip().split())
    S = Solution()
    print(S.bazinga(sorted(m)))