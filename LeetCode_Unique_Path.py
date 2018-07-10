class Solution:
    def __init__(self):
        self.d= {}
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        tab = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    tab[i][j]=1
                else:
                    tab[i][j]=tab[i-1][j] + tab[i][j-1]
        #print (tab)
        return tab[m-1][n-1]

'''
https://leetcode.com/problems/unique-paths/description/ 

Optimal Substructure:-
if i==0 or j==0:
    tab[i][j]=1
else:
    tab[i][j]=tab[i-1][j] + tab[i][j-1]                    
'''