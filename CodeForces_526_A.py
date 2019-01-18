from sys import stdin as si

class Solution:
    def bazinga(self,lst):
        x = [(k,v) for k,v in enumerate(lst) if k!=0]
        if x==[]:
            return 0
        mx = max(x, key=lambda x: x[1])
        base = mx[0] # floor
        total = 0
        for k,v in x:
            dis = 2* (abs(k-base) + k + base )
            print (k, base, dis)
            #up = base + k + abs(k-base)
            total += dis*v
        return total


if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    n = int(si.readline().strip())
    lst = list(map(int, si.readline().strip().split()))
    S = Solution()
    print(S.bazinga(lst))