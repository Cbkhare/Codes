class Solution:
    # @param A : root node of tree
    # @return an integer

    def minDepth(self, A):
        if not A.left and not A.right:
            return 1
        else:
            if A.left and A.right:
                return 1 + min(self.minDepth(A.left), self.minDepth(A.right))
            else:
                node = A.left if A.left else A.right
                return 1 + self.minDepth(node)