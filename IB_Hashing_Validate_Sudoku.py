class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        # self.m = [[int(x) if x!='.' else '' for x in AA] for AA in A]
        def get_box(i, j):
            i = i // 3
            j = j // 3
            return (i, j)

        def box(v, i, j):
            tup = get_box(i, j)
            if v in self.boxx[tup]:
                return True
            else:
                self.boxx[tup].add(v)
                return False

        # Hashes
        self.boxx = {(i, j): set() for i in range(3) for j in range(3)}
        self.r = {i: set() for i in range(1, 10)}
        self.c = {i: set() for i in range(1, 10)}

        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == '.':  continue
                val = A[i][j]

                if val in self.r[i + 1] or val in self.c[j + 1] or box(val, i,
                                                                       j):
                    return 0
                else:
                    self.r[i + 1].add(val)
                    self.c[j + 1].add(val)

        return 1

    def isValidSudoku_fast(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        seen = []

        for i, row in enumerate(board):
            for j, digit in enumerate(row):
                if digit != '.':
                    seen.append((i, digit))
                    seen.append((digit, j))
                    seen.append((i // 3, j // 3, digit))

        return len(seen) == len(set(seen))

'''
Only Validate
'''