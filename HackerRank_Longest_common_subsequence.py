from sys import stdin as si


class Solution():

    def lcs(self, X, Y, m, n):

        if m <0 or n<0:
           return '';
        if X[m] == Y[n]:
           return self.lcs(X, Y, m-1, n-1) + str(X[m])
        else:
           return max(self.lcs(X, Y, m, n-1), self.lcs(X, Y, m-1, n), key=lambda x: len(x))

if __name__ == "__main__":
    x = si.readline().strip()
    a = si.readline().strip()
    b = si.readline().strip()
    S=Solution()
    S.lcs(a, b, len(a), len(b))