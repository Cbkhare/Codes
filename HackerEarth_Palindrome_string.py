from sys import stdin as Si


class Solution(object):
    def __init__(self):
        self.d = {}

    def mainFun(self, A, b, e):
        if (b, e) in self.d: return
        self.d[(b, e)] = True
        if b >= e:
            return 0
        elif A[b:e + 1] == A[b:e + 1][::-1]:
            self.count += 1
        else:
            self.mainFun(A, b, e - 1);
            self.mainFun(A, b + 1, e);
            self.mainFun(A, b + 1, e - 1)
        return

    def mainFun1(self, A):
        self.count = 0
        self.mainFun(A, 0, len(A) - 1)
        return self.count


if __name__ == '__main__':
    A = Si.readline().strip()
    S = Solution()
    print(S.mainFun1(A) + len(A))

'''
https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/palindrome-count-1/description/'''