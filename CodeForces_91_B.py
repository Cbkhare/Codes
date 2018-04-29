#from sys import stdin as si


class Solution:

    def bazinga(self,n,m):
        r = [-1]*n
        # sorted(enumerate(m), key-itemgetter(1))
        m = sorted(range(len(m)), key= lambda k: m[k])
        mx = 0
        for i in range(n):
            mx = max(mx,m[i])
            r[m[i]] = mx - m[i] - 1
        print (*r)



if __name__ == '__main__':
    #for i in range(int(si.readline().strip())):
    '''
    n = int(si.readline().strip())
    #n,m = map(int, si.readline().strip().split())
    m = list(map(int, si.readline().strip().split()))
    S = Solution()
    S.bazinga(n,m)
    '''
    n = int(input().strip())
    #n,m = map(int, si.readline().strip().split())
    m = list(map(int, input().strip().split()))
    S = Solution()
    S.bazinga(n,m)


'''
http://codeforces.com/contest/91/problem/B


- Sort the list with respect to indexes
- Now Index list have to be iterated 
- We have to find the first number from to left to i, which is larger than i i.e
  in original list the number that appeared before the m[i] 
  Since the list is now sorted, the number occuring in the list provides the index
  which are smaller but higher in index. 
- For more, try replecating the solution with below 

- 7
- 10 4 6 3 2 8 15
- 4 2 1 0 -1 -1 -1
'''