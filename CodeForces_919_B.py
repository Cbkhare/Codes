from sys import stdin as si


class Solution:
    def bazinga(self,b):
        count = 1
        val = 19
        while True:
            if sum(map(int, str(val))) == 10:
                if count == b:
                    return val
                else:
                    count+=1
            val +=9


if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n = int(si.readline().strip())
    S = Solution()
    print(S.bazinga(n))
