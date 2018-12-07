class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if not A:
            return 0
        else:
            return 1 + max(self.maxDepth(A.left),self.maxDepth(A.right))