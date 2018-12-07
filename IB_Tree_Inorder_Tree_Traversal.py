class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def get_max_index(self, A, i, e):
        mx = A[i]
        mxi = i
        for j in range(i, e + 1):
            if A[j] > mx:
                mx = A[j]
                mxi = j
            return mxi

    def tree_builder(self, A, s, e):
        if s > e:
            return None
        else:

            mxi = self.get_max_index(A, s, e)
            root = TreeNode(A[mxi])
            root.left = self.tree_builder(A, s, mxi - 1)
            root.right = self.tree_builder(A, mxi + 1, e)
            return root

    def buildTree(self, A):
        root = self.tree_builder(A, 0, len(A) - 1)
        return root