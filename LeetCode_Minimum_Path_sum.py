class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.d = {}

    def sum(self,m,n):
        if (m,n) in self.d: return self.d.get((m,n))

        if m==0 and n==0:
            return self.grid[0][0]

        if m==0 and n>0:
            out = self.sum(m,n-1)
        elif m>0 and n==0:
            out = self.sum(m-1,n)
        else:
            out = min(self.sum(m-1,n), self.sum(m,n-1))
        self.d[(m,n)] = self.grid[m][n] + out
        return self.d[(m,n)]

'''
Optimal Substructure:-
min(self.sum(m-1,n), self.sum(m,n-1))
what is true for G[m][n] is also true for G[m-1][n] and G[m][n-1]. 
Hence is min is taken out, the True will persist. 

overlapping subproblems:-
solved with self.d
'''