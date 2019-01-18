class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or (not root.left and not root.right):
            return 0
        self.mx = -1

        def length(node):
            lf = rg = 0
            if not node.left and not node.right:
                return 1
            if node.left:
                lf = length(node.left)
            if node.right:
                rg = length(node.right)
            self.mx = max(self.mx, lf + rg + 1)  # lf+rg +1 if nodes are needed
            return max(lf, rg) + 1

        length(root)
        return self.mx - 1
