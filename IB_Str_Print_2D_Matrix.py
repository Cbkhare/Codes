from sys import stdin as si

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def fill_side(self, frm, A):
        upto = self.l - frm-1
        for i in range(self.l):
            print (frm, upto)
            if i<frm or i>upto: continue
            if i == frm or i == upto:
                self.M[i] = self.M[i][:frm] + [A] * (upto - frm + 1) + self.M[i][
                                                                   upto + 1:]
            else:
                self.M[i] = self.M[i][:frm] + [A] + self.M[i][frm+1:upto] + [A] +\
                    self.M[i][upto+1:]

    def prettyPrint(self, A):
        self.M = [[0]* (2 * A - 1)] * (2 * A - 1)
        self.l = 2 * A - 1
        for i in range(A, 0, -1):
            print (self.M)
            self.fill_side(A - i, i)
        return self.M

if __name__ == "__main__":
    S = Solution()
    test_cases = int(si.readline().strip())
    for _ in range(test_cases):
        print (S.prettyPrint(int(si.readline().strip())))

'''
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
'''