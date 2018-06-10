from sys import stdin as si


class Solution:
    def bazinga(self, s, k):
        while k>0:
            if s%10==0:
                s/=10
            else:
                s-=1
            k-=1
        return int(s)

if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    m,n = map(int,si.readline().strip().split())
    S = Solution()
    print (S.bazinga(m,n))
