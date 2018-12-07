from sys import stdin as si

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        self.count = 0
        self.d = d
        x = self.calc_pow(x,n)
        print (self.count)
        return self.decimate(x)

    def decimate(self,x):
        '''
        if x < 0:
            return (x+self.d) % self.d
        else:
            return x % self.d
        '''
        mod = abs(x) % self.d
        return mod if x >= 0 else self.d - mod

    def calc_pow(self, x, n):
        self.count += 1
        #print (x,n)
        if n == 0:
            return 1
        elif n == 1:
            return self.decimate(x)
        if n % 2 == 0:
            t = self.calc_pow(x, n//2)
            return self.decimate(t) * self.decimate(t)
        elif n % 2 != 0:
            t = self.calc_pow(x, n-1)
            return self.decimate(t) * self.decimate(x)


if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        #lst = list(map(int, si.readline().strip().split(', ')))
        l = int(si.readline().strip())
        m = int(si.readline().strip())
        n = int(si.readline().strip())
        print (S.pow(l,m,n))